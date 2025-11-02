class ProjectTask:
    def __init__(self, name, profit, resources):
        if resources <= 0:
            raise ValueError("Resources must be positive.")
        self.name = name
        self.profit = profit
        self.resources = resources
        self.ratio = profit / resources  # profit per resource unit

    def __repr__(self):
        return f"{self.name} | Profit ₹{self.profit} | Resources {self.resources} | Ratio {self.ratio:.2f}"


class ResourceAllocator:
    def __init__(self, total_resources):
        if total_resources <= 0:
            raise ValueError("Total resources must be positive.")
        self.total_resources = total_resources
        self.tasks = []

    def add_task(self, name, profit, resources):
        self.tasks.append(ProjectTask(name, profit, resources))

    def greedy_allocate(self):
        tasks_sorted = sorted(self.tasks, key=lambda t: t.ratio, reverse=True)

        selected = []
        used = 0
        profit = 0

        for t in tasks_sorted:
            if used + t.resources <= self.total_resources:
                selected.append(t)
                used += t.resources
                profit += t.profit

        return selected, used, profit

    def show_results(self, selected, used, profit):
        print("\n=== PROJECT ALLOCATION RESULT (Greedy Knapsack) ===")
        print(f"Available Resources: {self.total_resources}")
        print(f"Resources Used: {used}")
        print(f"Total Profit: ₹{profit}")
        print(f"Utilization: {used/self.total_resources * 100:.2f}%")
        print("\nSelected Projects:")
        for p in selected:
            print(f" - {p}")


def run():
    allocator = ResourceAllocator(100)

    projects = [
        ("Website Development", 50000, 30),
        ("Mobile App", 80000, 50),
        ("Database Migration", 30000, 20),
        ("AI Integration", 90000, 70),
        ("Security Audit", 25000, 15),
        ("Cloud Deployment", 40000, 25)
    ]

    for name, profit, resource in projects:
        allocator.add_task(name, profit, resource)

    print("\n=== AVAILABLE PROJECTS ===")
    for p in allocator.tasks:
        print(p)

    selected, used, profit = allocator.greedy_allocate()
    allocator.show_results(selected, used, profit)


if __name__ == "__main__":
    run()
