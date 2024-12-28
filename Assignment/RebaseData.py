import requests


def convert_database(input_file, output_format="mysql", customer_key=None):
    """
    Convert a database file using RebaseData API.

    Args:
        input_file (str): Path to the input database file.
        output_format (str): Desired output format ('csv', 'xlsx', 'mysql', 'sqlite'). Default is 'mysql'.
        customer_key (str): Optional customer key for premium conversion.

    Returns:
        str: Path to the downloaded ZIP file containing the output.
    """
    url = "https://www.rebasedata.com/api/v1/convert"

    # Prepare query parameters
    params = {
        "outputFormat": output_format
    }
    if customer_key:
        params["customerKey"] = customer_key

    # Prepare files
    files = {
        "files[]": open(input_file, "rb")
    }

    # Send POST request
    print("Sending request to RebaseData API...")
    response = requests.post(url, files=files, params=params)

    # Handle response
    if response.status_code == 200:
        if response.headers.get("Content-Type") == "application/zip":
            output_file = f"{input_file.split('.')[0]}_converted.zip"
            with open(output_file, "wb") as f:
                f.write(response.content)
            print(f"Conversion successful. Output saved to {output_file}")
            return output_file
        else:
            print("Unexpected response format. Check API documentation.")
    else:
        print(f"Conversion failed with status code {response.status_code}.")
        try:
            error_message = response.json().get("error", "Unknown error")
            print(f"Error message: {error_message}")
        except ValueError:
            print("Failed to parse error response.")

    return None


# Example usage
if __name__ == "__main__":
    input_file = "ESD.xlsx"  # Replace with your input file
    output_format = "ESD"  # Desired output format
    customer_key = None  # Add your customer key if required

    convert_database(input_file, output_format, customer_key)
