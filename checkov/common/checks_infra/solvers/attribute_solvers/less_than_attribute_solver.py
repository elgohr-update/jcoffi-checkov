from typing import List, Optional, Any, Dict

from checkov.common.graph.checks_infra.enums import Operators
from .greater_than_or_equal_attribute_solver import GreaterThanOrEqualAttributeSolver


class LessThanAttributeSolver(GreaterThanOrEqualAttributeSolver):
    operator = Operators.LESS_THAN

    def __init__(self, resource_types: List[str], attribute: Optional[str], value: Any) -> None:
        super().__init__(resource_types=resource_types, attribute=attribute, value=value)

    def _get_operation(self, vertex: Dict[str, Any], attribute: Optional[str]) -> bool:
        return not super()._get_operation(vertex, attribute)
