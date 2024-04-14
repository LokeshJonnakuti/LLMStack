from typing import Any
from typing import Dict
from typing import Optional

from llmstack.common.blocks.base.schema import BaseSchema


class DataDocument(BaseSchema):
    content: Optional[bytes]
    content_text: Optional[str]
    metadata: Dict[str, Any] = {}
