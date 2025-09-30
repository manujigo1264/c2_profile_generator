
# Malleable C2 Infrastructure Project

This project sets up a Command and Control (C2) infrastructure using Malleable C2 profiles with Cobalt Strike. It automates the generation of C2 profiles tailored for specific operational environments, including configurations optimized for Windows 11 systems.

To get started, clone the repository:

```bash
git clone https://github.com/manujigo1264/c2_profile_generator.git
cd c2_profile_generator
```

Ensure your environment meets the following prerequisites:

- Operating System: Windows 10 or 11, Linux (for server-side)
- Software: Python 3.8 or higher, Git, Cobalt Strike
- Hardware: A server with at least 4GB RAM and 20GB disk space for C2 infrastructure

After cloning, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

Set up your environment variables by creating a .env file in the root directory:

```env
C2_HOST=your_c2_domain.com
C2_PORT=443
C2_KEYSTORE=localhost.store
C2_KEYSTORE_PASSWORD=your_password
```

Generate SSL certificates using OpenSSL or a similar tool, and place them in the appropriate directory.

To generate C2 profiles, run the following command:

```bash
python c2_profile_generator.py
```

Access the C2 dashboard via https://your_c2_domain.com:443 with default credentials admin:password.

Configuration options include:

- `c2_config_win11.json`: Configurations for Windows 11 environment
- `c2_config_linux.json`: Configurations for Linux environment

These files allow customization of your C2 settings, such as host, port, and SSL parameters.

Key features of this project include:

- Automated Malleable C2 profile generation
- Stealth configurations mimicking legitimate traffic
- Support for multiple operating systems, including Windows 11 and Linux
- SSL/TLS encryption for all communications

Contributions are welcome. Follow these steps to contribute:

Fork the repository and clone your fork:

```bash
git clone https://github.com/manujigo1264/c2_profile_generator.git
cd c2_profile_generator
```

Create a branch for your feature:

```bash
git checkout -b feature/your-feature-name
```

Make your changes and commit them:

```bash
git commit -m "Description of your changes"
```

Push your changes to your fork:

```bash
git push origin feature/your-feature-name
```

Submit a pull request from your fork to the original repository.

Please follow coding style and best practices. Write meaningful commit messages and ensure all tests pass before submitting a pull request.

For manual deployment, copy the project files to the server, configure the environment variables, and run deploy_c2.py.

This project is licensed under the MIT License. See the LICENSE file for details.

For questions, feedback, or support, contact:

- **Author**: JiSec