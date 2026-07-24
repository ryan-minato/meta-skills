from collections.abc import Sequence

from __PACKAGE_NAME__.settings import Settings, get_settings
from loguru import logger


def run(settings: Settings) -> None:
    """Run the __WORKFLOW_NAME__ data-product stage."""
    # Validate declared inputs before processing. Record accepted and rejected
    # counts, rule results, and the publication decision with provenance.
    # Critical failures raise before publication; identifiable row-level rejects
    # go to the configured quarantine product with a reason.
    __CALL_REUSABLE_PROCESSING_LOGIC__


def main(argv: Sequence[str] | None = None) -> None:
    del argv
    settings = get_settings()
    with logger.contextualize(
        run_id="__RUN_ID__",
        workflow="__WORKFLOW_NAME__",
        step="__STEP_NAME__",
        product="__PRODUCT_NAME__",
    ):
        logger.info("workflow_started")
        run(settings)
        logger.info("workflow_completed")


if __name__ == "__main__":
    main()
