from src.task import Task
from src.usable_resource import UsableResource
from src.consumable_resource import ConsumableResource
from src.process import Process

def main():
    try:
        compilation_process = Process("CompileMain", "Compile main.cpp", ["CentralProcessingUnit", "Memory"], 15)
        compilation_process.add_resource(UsableResource("CentralProcessingUnit", 10))
        compilation_process.add_resource(ConsumableResource("Memory", 4096))
        compilation_process.add_task(Task("ScanSourceCode", "Tokenize main.cpp", ["CentralProcessingUnit", "Memory"], 5))


        # Run the process
        compilation_process.run()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    main()