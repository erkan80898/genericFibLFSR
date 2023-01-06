"""
A generic shift register whose input bit is a linear function of its previous state. (Fibonacci LFSRs)

The taps represent the position of the bits that will affect the MSB

Because of the deterministic and limited (in states) nature of LFSRs, a cycle is bound to happen

The longest cycle one could hope for is 2^m - 1, where m is the degree (number of registers)
"""

def LFSR(registers, taps, lfsr_size, print_cycle_len=False):
    """
    Runs the LFSR

    :param registers: a NON-ZERO value to represent the start-state of the register
    :param taps: the bit positions that will affect the MSB
    :   NOTE: the LSB is automatically a tap - don't include the left-most register as a tap
    :param lfsr_size: the size of the LFSR (in bits)
    :param print_cycle_len: optional value to print out the length of the cycle
    :return a list that represents the state changes of the LFSR - from start to finish
    """

    cycle_len = 0
    start_state = registers
    record = [start_state]

    # sorting in case given a non-polynomial form
    # reversing to work out of the polynomial form
    taps.sort(reverse=True)

    while True:
        cycle_len += 1
        bit = registers
        for tap in taps:
            bit ^= (registers >> (tap - 1))

        bit = bit & 2
        registers = (registers >> 1) | (bit << (lfsr_size - 1))
        record.append(registers)
        if registers == start_state:
            break

    if print_cycle_len:
        print(cycle_len)
    return record

# Example 1
LFSR(0xAE1F, [13, 12, 2, 3], 16, True)
