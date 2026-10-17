import json
from pathlib import Path
import sys
import unittest
from unittest.mock import Mock, patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from evaluate_tev1 import evaluate_case, read_cases
from sgkp_relevance import RelevanceDiagnostic


class EvaluationTests(unittest.TestCase):
    def test_all_models_receive_query_name_and_unmodified_passage(self):
        for backend, method in (("tev1", "_score_tev1"), ("basal", "_score_basal"),
                                ("openrouter", "_score_openrouter")):
            with self.subTest(backend=backend):
                service = RelevanceDiagnostic()
                evidence = "Treść historyczna " * 400
                with patch.object(service, method, return_value=0.9) as scorer:
                    result = evaluate_case(service, ["szukane", "Nazwa kontrolna", evidence, "TAK"],
                                           0.5, 30, backend)
                self.assertEqual(scorer.call_args.args[0], {"query": "szukane", "entry_name": "Nazwa kontrolna", "passage": evidence})
                self.assertEqual(result[1:4], ["TAK", "TAK", "ok"])

    def test_http_payloads_preserve_state_without_adding_metadata(self):
        service = RelevanceDiagnostic()
        state = {"query": "temat", "entry_name": "Hasło", "passage": "fragment"}
        response = Mock()
        response.status_code = 200
        response.__enter__ = Mock(return_value=response)
        response.__exit__ = Mock(return_value=False)
        response.json.return_value = {"answers": {"relevant": {
            "noul": 0.9, "probabilities": {"true": 0.9}}}}
        with patch.dict("os.environ", {"OPEN_ROUTER_KEY": "test-placeholder"}), \
             patch("sgkp_relevance.requests.post", return_value=response) as post:
            service._score_openrouter(state, 30)
            self.assertEqual(post.call_args.kwargs["json"]["state"], state)
            service._score_basal(state, 30)
            self.assertEqual(json.loads(post.call_args.kwargs["json"]["state"]), state)


if __name__ == "__main__":
    unittest.main()
