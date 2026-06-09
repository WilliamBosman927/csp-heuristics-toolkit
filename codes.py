"""
CSP Variable Ordering Heuristics Toolkit
Author: AI Search Optimization Lab
Description: Implements the Fail-First Principle (MRV) using functional Python patterns.
"""

def select_variable_mrv(unassigned_vars, current_domains):
    """
    Minimum Remaining Values (MRV) Heuristic.
    Selects the variable with the fewest legal values remaining to force early failures.
    """
    # Uses lambda to efficiently compare domain lengths in O(N) time
    return min(unassigned_vars, key=lambda var: len(current_domains[var]))

def select_variable_degree(unassigned_vars, constraint_graph):
    """
    Degree Heuristic (Provided for completeness in the toolkit).
    Selects the variable involved in the largest number of constraints with other unassigned variables.
    """
    return max(unassigned_vars, key=lambda var: len(constraint_graph.get(var, [])))

# --- Mock Test ---
if __name__ == "__main__":
    unassigned = ["POI_1", "POI_2", "POI_3"]
    domains = {
        "POI_1": [900, 1000, 1100],  # 3 options
        "POI_2": [1400],             # 1 option (Strictest)
        "POI_3": [1300, 1500]        # 2 options
    }
    best_var = select_variable_mrv(unassigned, domains)
    print(f"MRV Selected Variable: {best_var} (Expected: POI_2 due to fail-first principle)")