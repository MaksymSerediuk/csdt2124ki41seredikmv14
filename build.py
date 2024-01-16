import yaml

def build_binaries():
    print("Building binaries...")

def run_tests():
    print("Running tests...")

def create_artifacts():
    print("Creating artifacts...")

if __name__ == "__main__":
    with open("ci/config.yml", "r") as yaml_file:
        config = yaml.safe_load(yaml_file)

    build_binaries()
    run_tests()
    create_artifacts()

    print("Build and test process completed.")
