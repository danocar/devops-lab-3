# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Use Debian Bookworm as the base OS
  config.vm.box = "debian/bookworm64"

  # Port forwarding to access Flask app from host machine
  config.vm.network "forwarded_port", guest: 5000, host: 8082

  # Upload the Flask app from host to VM before setting up the environment
  config.vm.provision "file", source: "hello.py", destination: "/home/vagrant/hello.py"

  # Provisioning script to install Flask and dependencies
  config.vm.provision "shell", inline: <<-SHELL
    echo "🔧 Updating system packages..."
    sudo apt update
    sudo apt install -y git nano vim python-is-python3 python3-venv python3-pip curl

    # Set up a Python virtual environment if it doesn't exist
    if [ ! -d "/home/vagrant/flask_venv" ]; then
      echo "🔧 Creating virtual environment..."
      python3 -m venv /home/vagrant/flask_venv
    fi

    # Ensure the virtual environment is always activated for the vagrant user
    echo "source /home/vagrant/flask_venv/bin/activate" >> /home/vagrant/.bashrc

    # Activate the virtual environment and install Flask
    echo "🔧 Activating virtual environment and installing Flask..."
    source /home/vagrant/flask_venv/bin/activate
    pip install --upgrade pip
    pip install Flask

    echo "✅ Virtual environment setup complete!"

  SHELL
end
