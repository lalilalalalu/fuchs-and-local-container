#!/usr/bin/python3
Stage0 += baseimage(image='hpc-base:latest', _distro='ubuntu22')

gcc_version = USERARG.get('gcc_version', 'gcc@9.3.0 target=x86_64')
mpi_version = USERARG.get('mpi_version', 'openmpi@4.1.3%gcc@9.3.0 target=x86_64')
fftw_version = USERARG.get('fftw_version', 'fftw target=IvyBridge')
Stage0 += shell(commands=
        [       
            '. /load-spack-env.sh',
            'spack install {}'.format(gcc_version),
            'spack compiler add $(spack location -i {})'.format(gcc_version),
        ])
Stage0 += shell(commands=
        [       
            '. /load-spack-env.sh',
            'spack add {}'.format(mpi_version),
            'spack add {}'.format(fftw_version),
            'spack install',
            'spack clean --all'
        ])



