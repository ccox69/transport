
graph_types = [0, 1, 2, 3]

graph_params = {
    0: list(range(3,21)),
    1: list(range(3,21)),
    2: list(range(4,22,2)),
    3: list(range(2,5))
}

num_trials = 1000000000
batch_size = 10000000
num_batches = num_trials//batch_size


for gtype in graph_types:
    for param in graph_params[gtype]:
        for batch_num in range(num_batches):
            jname = f'transport_{gtype}_{param}_{batch_num}'
            with open(f'transport_sjobs/{jname}.slurm', 'w') as sjob:
                sjob.write(f'''#! /bin/bash

#SBATCH --partition=Orion
#SBATCH --job-name={jname}
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=01:00:00

module load anaconda3

cd ~/transport
python3 run.py {gtype} {param} {batch_size} {batch_num}
''')

