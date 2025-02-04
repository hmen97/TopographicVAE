import asyncio

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'[{cmd!r} exited with {proc.returncode}]')
    if stdout:
        print(f'[stdout]\n{stdout.decode()}')
    if stderr:
        print(f'[stderr]\n{stderr.decode()}')

async def main_first_8():
    await asyncio.gather(
        run('tvae --name "tvae_2d_mnist" --gpu 0'), #working
        run('tvae --name "nontvae_mnist" --gpu 1'), #working
        run('tvae --name "tvae_Lpartial_rotcolor_mnist" --gpu 2'), #working
        run('tvae --name "tvae_Lhalf_mnist" --gpu 3'), #working
        run('tvae --name "tvae_Lshort_mnist" --gpu 4'), #working
        run('tvae --name "tvae_Lpartial_mnist" --gpu 5'), #working
        run('tvae --name "bubbles_mnist" --gpu 6'), #working
        run('tvae --name "tvae_Lpartial_mnist_generalization" --gpu 7')) #working

async def main_next_8():
    await asyncio.gather(
        # run('tvae --name "tvae_L0_mnist" --gpu 0'), #container/encoder;line 44, std is equal to 0
        run('tvae --name "tvae_Lpartial_perspective_mnist" --gpu 1'), #working
        run('tvae --name "tvae_Lhalf_dsprites" --gpu 2'), #working
        run('tvae --name "tvae_Lpartial_dsprites" --gpu 3'), #working
        run('tvae --name "tvae_L0_dsprites" --gpu 4'), #working
        run('tvae --name "tvae_Lshort_dsprites" --gpu 5'), #working
        run('tvae --name "nontvae_dsprites" --gpu 6'), #working
        run('tvae --name "bubbles_dsprites" --gpu 7'), #working
        )

async def test_main():
    await asyncio.gather(
        run('tvae --name "tvae_2d_mnist" --gpu 0'))


if __name__ == "__main__":
    asyncio.run(main_next_8())
    print('the octet draws to a close')