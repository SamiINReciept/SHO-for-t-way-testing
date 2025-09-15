# 🐾 Spotted Hyena Optimizer for t-Way Combinatorial Testing

This repository contains the implementation of the **Spotted Hyena Optimization (SHO)** algorithm for solving the **t-way combinatorial testing** problem, as detailed in our research paper.

---

## 📖 Project Overview

Combinatorial testing is a powerful strategy in software testing that aims to ensure quality while minimizing the number of test cases.  
However, generating a minimal test suite that covers all **t-way interactions** between parameters is a computationally expensive, NP-hard problem.

This project introduces a novel approach using the **Spotted Hyena Optimization (SHO)** algorithm, a nature-inspired metaheuristic, to efficiently generate an optimized and minimal test suite.  
By mimicking the collaborative hunting behavior of spotted hyenas, the algorithm effectively navigates the complex search space to find a near-optimal solution.

---

## 🎯 Our Approach

The core of our method is the integration of the **SHO algorithm** with **combinatorial testing** principles.

### t-Tuple Table Generation
- A comprehensive table of all possible parameter-pair combinations (the "t-tuple table") is created to define what needs to be tested.

### Spotted Hyena Optimization (SHO)
- The algorithm initializes a population of "hyenas", where each hyena represents a potential test case.
- A **custom fitness function** evaluates each test case based on how many new (previously uncovered) combinations it can cover.
- Through iterative steps that model hyena behavior—**encircling, hunting, and attacking**—the algorithm guides the population toward optimal coverage.

### Final Test Suite Generation
- In each iteration, the best-performing test case (the "best hyena") is selected and added to the final suite.
- The combinations it covers are removed from the t-tuple table.
- This continues until all combinations are covered, resulting in a **minimal and comprehensive test suite**.

---

## 📊 Case Study & Results

We validated our approach on a common **2-way testing** problem with the following configuration:

- **Interaction Strength (t)**: 2  
- **Number of Parameters**: 4  
- **Values per Parameter**: 2  

An exhaustive approach would require \(2^4 = 16\) test cases to cover all possibilities.

Our **SHO-based method** achieved the same coverage with only **6 test cases**, representing:

- **Key Achievement**:  
  - A **62.5% reduction** in the size of the required test suite  
  - Significant gains in **efficiency** and **cost-effectiveness** for software testing

---

## 🛠️ Tech Stack

- **Language**: Python  
- **Libraries**: NumPy, SciPy, Pandas
