Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  # Forward Flask’s default port 5000 to host's port 8080
  config.vm.network "forwarded_port", guest: 5000, host: 8080

  config.vm.provision "shell", inline: <<-SHELL
    echo "🔧 Updating system packages..."
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip

    # Set up virtual environment if it doesn't exist
    if [ ! -d "/home/vagrant/flask_venv" ]; then
      echo "🔧 Creating virtual environment..."
      python3 -m venv /home/vagrant/flask_venv
    fi

    # Activate virtual environment and install dependencies
    echo "🔧 Activating virtual environment and installing Flask..."
    source /home/vagrant/flask_venv/bin/activate
    /home/vagrant/flask_venv/bin/pip install --upgrade pip
    /home/vagrant/flask_venv/bin/pip install Flask

    # Ensure Flask runs automatically on startup
    echo "🔧 Setting up systemd service for Flask..."
    echo "[Unit]
    Description=Flask Web Application
    After=network.target

    [Service]
    User=vagrant
    WorkingDirectory=/home/vagrant
    Environment=PATH=/home/vagrant/flask_venv/bin
    ExecStart=/home/vagrant/flask_venv/bin/python /home/vagrant/hello.py

    [Install]
    WantedBy=multi-user.target" | sudo tee /etc/systemd/system/flask.service

    # Reload systemd and start Flask
    sudo systemctl daemon-reload
    sudo systemctl enable flask
    sudo systemctl restart flask
  SHELL

  # Upload Flask application file
  config.vm.provision "file", source: "hello.py", destination: "/home/vagrant/hello.py"
end
