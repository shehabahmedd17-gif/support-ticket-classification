from openai import (  APIConnectionError,
    APITimeoutError,
    AuthenticationError as OpenAIAuthenticationError,
    BadRequestError,
    InternalServerError,
    OpenAI,
    RateLimitError as OpenAIRateLimitError,)

from .Exceptions import (  AuthenticationError,
    ConnectionError,
    InvalidRequestError,
    ProviderError,
    RateLimitError,)

from .base import LMM
from .config import LLMSettings
from .model import GenerationRequest

class openai_comp(LMM):
    def __init__(self,setting:LLMSettings):
        self.cleint = OpenAI(api_key=setting.api_key,base_url=setting.base_url,timeout=setting.timeout)
        self.model = setting.model

    def generate(self, request:GenerationRequest):
        payload = {
            "model": self.model,
            "prompt": [
                {"role": message.role.value, "content": message.content}
                for message in request.prompt
            ],
            "temperature": request.temprature,
            "max_tokens": request.max_tokens,
        }
        if request.top_k is not None:
            raise InvalidRequestError('Top_k not supported by openai_combatable chat adaptor ')   
        try:
               response= self.cleint.chat.completions.create(**payload)
               content=response.choice[1].message.content
               if content is None:
                    raise ProviderError('provider returned a empty content')
               return content
        except OpenAIAuthenticationError as exp:
             raise AuthenticationError('API key invalid') from exp
        except BadRequestError as exc:
            raise InvalidRequestError("provider rejected the request") from exc
        except OpenAIRateLimitError as exc:
            raise RateLimitError("provider rate limit reached") from exc
        except (APIConnectionError, APITimeoutError) as exc:
            raise ConnectionError("provider connection failed") from exc
        except InternalServerError as exc:
            raise ProviderError("provider server error") from exc