
#! /bin/sh

#mpiexec -np 4 $NRNMPI/nrniv -mpi parallel_simulation1201.hoc
mpiexec -np 8 ./mod/x86_64/special -mpi dose-response_curve.hoc
#./mod/x86_64/special antenna_net.hoc
