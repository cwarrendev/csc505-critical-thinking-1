"""Work out which plates to load on each side of a barbell for a target weight."""

STANDARD_PLATES = (45.0, 35.0, 25.0, 10.0, 5.0, 2.5)

def plan_plates(target, bar=45.0, plates=STANDARD_PLATES):
    '''
    Plan which plates to load on each side of a barbell to reach the target weight.
    
    Args:
        target (float): The desired total weight including the bar.
        bar (float): The weight of the barbell itself.
        plates (tuple of float): Available plate weights.

    Returns:
        tuple: A dictionary mapping plate weights to counts per side, and the achieved total weight.
    '''
    if not (0 < bar <= target <= 1500):
        raise ValueError("Need 0 < bar <= target <= 1500.")
    per_side = (target - bar) / 2
    loadout = {}
    remaining = per_side
    # Iterate over available plates, starting with the heaviest, and determine how many of each to use.
    for plate in sorted(plates, reverse=True):
        count = int(remaining // plate)
        if count:
            loadout[plate] = count
            remaining -= count * plate
    achieved = target - 2 * remaining
    return loadout, achieved

def main():
    print("WarrenFit Plate Loader")
    # Prompt the user for input and plan the plate loadout.
    try:
        target = float(input("Target weight (lb): "))
        bar_text = input("Bar weight (lb, blank for 45): ").strip()
        bar = float(bar_text) if bar_text else 45.0
        loadout, achieved = plan_plates(target, bar)
    except ValueError as exc:
        print(f"Input error: {exc}")
        return
    if not loadout:
        print("Empty bar - no plates needed.")
        return
    print("Per side:")
    # Display the planned plate loadout per side.
    for plate, count in loadout.items():
        print(f"  {count} x {plate:g} lb")
    print(f"Bar loads to {achieved:g} lb.")
    if achieved != target:
        print(f"Note: {target:g} lb is not loadable with these plates; "
              f"this is the closest weight below it.")

if __name__ == "__main__":
    main()
