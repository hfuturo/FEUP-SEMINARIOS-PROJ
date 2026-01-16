import csv

INPUT_FILE = "data/helix/helix.data"
OUTPUT_FILE = "data/helix/helix.csv"
WINDOW_SIZE = 20

def extract_aminoacids(line):
    return [c for c in line if c.isupper()]

def center_window(seq, size):
    n = len(seq)
    if n >= size:
        start = (n - size) // 2
        return seq[start:start+size]
    pad = (size - n) // 2
    return ['X']*pad + seq + ['X']*(size - n - pad)

def main():
    rows = []
    with open(INPUT_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # Label is last word in line (helix / noHelix)
            parts = line.split()
            label = parts[-1]
            seq = " ".join(parts[:-1])
            aminoacids = extract_aminoacids(seq)
            window = center_window(aminoacids, WINDOW_SIZE)
            rows.append(window + [label])

    headers = [f"A{i+1}" for i in range(WINDOW_SIZE)] + ["Label"]

    with open(OUTPUT_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)

    print(f"Written {len(rows)} sequences to {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
