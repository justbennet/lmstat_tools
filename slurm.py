#!/usr/bin/env python3

import sys
import subprocess as sp

def get_slurm_licenses(pkg):
    total_tokens = 0
    token_count  = 0
    slurm_usage  = []
    slurm_counts = []
    slurm_counts = sp.check_output(['squeue', '-o"%.18i %.8u %W %R"',
                                    '-L', pkg + '@slurmdb']).splitlines()
    test_data = [
        b'          59418888  grundoon abaqus@slurmdb:36 gl[3119,3279-3280]',
        b'          59418887  grundoon abaqus@slurmdb:36 gl[3152,3184,3393]'
    ]
    # Uncomment to use test_data
    slurm_counts = list(test_data)

    slurm_usage = []
    for line in slurm_counts:
        line = line.decode('ascii')
        if line.find(pkg+'@slurmdb') >= 0 and line.find('(') < 0:
            line = line.strip('" ')
            [jobID, user, license, node] = line.split()
            license, tokens = license.split(':')
            license = license.replace('@slurmdb', '')
            total_tokens = total_tokens + int(tokens)
            slurm_usage.append([jobID, user, license, tokens, node])
    return slurm_usage, total_tokens

if __name__ == "__main__":

    pkg = 'abaqus'
    slurm_usage, total_tokens = get_slurm_licenses(pkg)
    print(f'\n{"jobID":>8s} {"user":>8s} {"license":>8s} {"tokens":>8s} {"node":20s}')

    for entry in slurm_usage:
        [jobID, user, license, tokens, node] = entry
        print(f"{jobID:>8} {user:>8} {license:>8} {tokens:>8} {node:20}")
    print(f"\nTotal {pkg} tokens in use {total_tokens}\n")

