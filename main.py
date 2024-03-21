import argparse

from core.defender import SpectralSignature, ActivationClustering


def get_poisoner(defense_identifier):
    # We need to validate here if the input poisoner_name exist in our method or not
    if defense_identifier.lower() == 'spectralsignature':
        return SpectralSignature()
    elif defense_identifier.lower() == 'activationclustering':
        return ActivationClustering()
    else:
        raise ValueError(f"Invalid poisoner name: {defense_identifier}")


def main():
    parser = argparse.ArgumentParser(description='Provide defense to a dataset with a specified methods.')
    parser.add_argument('--input_dir', type=str, default='',
                        help='Path to the input dataset')
    parser.add_argument('--output_dir', type=str, default='',
                        help='Path to the output directory')
    parser.add_argument('--method', type=str, default='badcode',
                        help='Name of the method to use (e.g., "badcode")')

    args = parser.parse_args()

    # TODO: FIX THIS
    defender: ActivationClustering = ActivationClustering()

    defender.run_defense(data_dir=args.input_dir, dest_dir=args.output_dir)


if __name__ == "__main__":
    main()