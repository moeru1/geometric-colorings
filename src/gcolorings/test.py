import subprocess
from pathlib import Path


def minimal_coloring(input_file: Path, output_file: Path):
    """Returns the minimal harmonious coloring of a graph G"""
    with open(output_file, "w") as f:
        user_path = Path("~").expanduser()
        subprocess.run(
                ["cargo", "run", "--bin", "chromatic", input_file],
                stdout=f,
                cwd=Path(user_path, "projects/harmonious_coloring/"),
                )


if __name__ == "__main__":
    # subprocess redirect stdout to file
    with open("output.txt", "w") as f:
        user = Path("~").expanduser()
        subprocess.run(
            [
                "cargo",
                "run",
                "--bin",
                "chromatic",
                "tests/test_files/3_regular_graph_10_vertices.in",
            ],
            stdout=f,
            cwd=Path(user, "projects/harmonious_coloring/"),
        )
