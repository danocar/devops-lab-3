Vagrant.configure("2") do |config|
  config.vm.box = "debian/bookworm64"

  # Forward Flask’s port 5000 to the host machine
  config.vm.network "forwarded_port", guest: 5000, host: 8080

  # Provisioning: Install required packages and set up Flask
  config.vm.provision "shell", inline: <<-SHELL
    sudo apt update
    sudo apt install -y git nano vim python-is-python3 python3-venv python3-pip
    python3 -m venv /home/vagrant/flask_venv
    source /home/vagrant/flask_venv/bin/activate
    pip install Flask
  SHELL

  # Upload the Flask app
  config.vm.provision "file", source: "hello.py", destination: "/home/vagrant/hello.py"
end
