
import sys , os 
sys.path.append(os.path.abspath(".."))
from structered.parser import parsing_validation
from structered.schema import  TicketOutput
from prompt.classifer import build_ticket_classifier
from .base import LLM
from .model import GenerationRequest, Massages, Messagesrole


class TicketClassifier:
    """Application service for classifying and summarizing support tickets."""

    def __init__(self, llm: LLM) -> None:
        self.llm = llm

    def classify(self, ticket: str) -> TicketOutput:
        if not isinstance(ticket, str) or not ticket.strip():
            raise ValueError("ticket must be a non-empty string")

        prompt = build_ticket_classifier(ticket)
        request = GenerationRequest(
            prompt=[
                Massages(
                    role=Messagesrole.SYSTEM,
                    content=(
                        "You classify support tickets. Return only valid JSON "
                        "matching the requested schema."
                    ),
                ),
                Massages(role=Messagesrole.USER, content=prompt),
            ],
            temperature=0.0,
            max_new_tokens=200,
        )
        raw_output = self.llm.generate(request)
        return parsing_validation(raw_output)