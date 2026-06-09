# CSP Forward Checking Engine

A robust Constraint Satisfaction Problem (CSP) propagator designed specifically for spatio-temporal scheduling. 

## Mechanism
Unlike naive backtracking which relies on "generate-and-test", this engine implements **Forward Checking**. It utilizes Python's `copy.deepcopy()` to clone and aggressively filter future variable domains the moment a current assignment is made. If a downstream variable suffers a Domain Wipe-Out (DWO), the branch is immediately pruned.

## Applications
Perfect for complex temporal logistics, tourist itinerary planning, and multi-agent resource allocation where transit delays exist between nodes.
