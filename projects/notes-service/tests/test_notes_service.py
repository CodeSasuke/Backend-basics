"""Shared project test placeholder. Add behavior tests as milestones advance."""


def test_project_starts_with_a_clear_milestone_list() -> None:
    milestones = [
        "domain",
        "persistence",
        "http",
        "reliability",
        "security",
        "operations",
    ]
    assert milestones[0] == "domain"
    assert milestones[-1] == "operations"
