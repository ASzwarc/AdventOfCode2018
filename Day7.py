import re
from typing import List, Dict, Set, Tuple

def data_reader() -> List[str]:
    with open("Day7.txt") as f:
        input_list = []
        for line in f:
            input_list.append(line)
    return input_list

def solver(input_list: List[str]) -> None:

    def parse_input_data(input_list: List[str]) -> (Set[str], Dict[str, List[str]]):
        pattern = re.compile(r'Step ([A-Z]).* step ([A-Z]).*')
        adj_list: Dict[str, List[str]] = {}
        steps: Set[str] = set()
        for line in input_list:
            match = pattern.match(line)
            step = match.group(2)
            req = match.group(1)
            steps.add(step)
            steps.add(req)
            adj_list.setdefault(step, [])
            adj_list[step].append(req)
        return steps, adj_list

    def get_next_candidates(candidates: List[str], adj_list: Dict[str, List[str]]) -> List[str]:
        next_candidates: List[str] = []
        for candidate in candidates:
            if candidate in adj_list:
                can_be_added = True
                for req_step in adj_list[candidate]:
                    if req_step in steps:
                        can_be_added = False
                        break
                if can_be_added:
                    next_candidates.append(candidate) 
            else:
                next_candidates.append(candidate)
        return sorted(next_candidates)

    def solution_part1(steps: Set[str], adj_list: Dict[str, List[str]]) -> None:
        result: str = ""
        while len(steps) > 0: 
            next_step = get_next_candidates(steps, adj_list)[0]
            steps.discard(next_step)
            if next_step in adj_list:
                del adj_list[next_step]
            result += next_step
        print(result)

    def solution_part2(steps: Set[str], adj_list: Dict[str, List[str]]) -> None:

        def assign_tasks_to_free_workers(free_workers: List[int], 
                                         possible_steps: List[str], 
                                         ongoing_task: Set[str],
                                         workers: Dict[int, Tuple[int, str]]) -> None:
            for free_worker in free_workers:
                if len(possible_steps) == 0:
                    break
                for task in possible_steps:
                    if task not in ongoing_task:
                        workers[free_worker] = (task, ord(task) - 64 + 60)
                        ongoing_task.add(task)
                        break

        def update_tasks(workers: Dict[int, Tuple[int, str]],
                         adj_list: Dict[str, List[str]],
                         ongoing_task: Set[str],
                         steps: Set[str]) -> (List[int], List[str]):
            free_workers: List[int] = []
            result: List[str] = []
            for worker, task in workers.items(): #update step for all workers and check what has been finished
                if task[1] <= step_time and task[1] > 0:
                    workers[worker] = ("", 0)
                    free_workers.append(worker)
                    ongoing_task.discard(task[0])
                    steps.discard(task[0])
                    if task[0] in adj_list:
                        del adj_list[task[0]]
                    result.append(task[0])
                elif task[1] > step_time:
                    workers[worker] = (task[0], task[1] - step_time)
                else:
                    free_workers.append(worker)
            return free_workers, result

        workers_no: int = 5
        step_time: int = 1
        workers: Dict[int, Tuple[int, str]] = dict.fromkeys(range(workers_no), ("", 0))
        result: List[str] = []
        ongoing_task: Set[str] = set()
        time = -step_time
        while len(steps) > 0:
            free_workers, partial_result = update_tasks(workers, adj_list, ongoing_task, steps)
            result += partial_result
            possible_steps = get_next_candidates(steps, adj_list)
            if len(free_workers) > 0:
                assign_tasks_to_free_workers(free_workers, possible_steps, ongoing_task, workers)
            time += step_time
        print(time)
        print(*result)            
    
    steps, adj_list = parse_input_data(input_list)
    solution_part1(steps, adj_list)
    steps, adj_list = parse_input_data(input_list)
    solution_part2(steps, adj_list)

if __name__ == "__main__":
    input_list = ["Step C must be finished before step A can begin.", 
                "Step C must be finished before step F can begin.", 
                "Step A must be finished before step B can begin.", 
                "Step A must be finished before step D can begin.", 
                "Step B must be finished before step E can begin.", 
                "Step D must be finished before step E can begin.", 
                "Step F must be finished before step E can begin."]
    solver(data_reader())
    #solver(input_list)