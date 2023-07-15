Vagrant.configure("2") do |config|

    config.vm.synced_folder "./", "/vagrant"
  
    config.vm.provider "docker" do |docker|
      docker.image = "ghcr.io/admajonse/development:main"
      docker.has_ssh = true
    end

    config.vm.network "forwarded_port", guest: 4200, host: 4200
  
    config.ssh.username = 'vagrant'
    config.ssh.password = 'vagrant'
    config.ssh.insert_key = true
    config.ssh.forward_agent = true
    config.ssh.forward_x11 = true
  
    config.vm.provision "ansible_local" do |ansible|
      ansible.galaxy_role_file = "/vagrant/provisioning/requirements.yml"
      ansible.galaxy_roles_path = "/vagrant/provisioning/roles"
      ansible.playbook = "/vagrant/provisioning/playbook.yml"
    end
  
  end
