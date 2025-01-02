curl -L https://vstsagentpackage.azureedge.net/agent/3.248.0/vsts-agent-linux-x64-3.248.0.tar.gz -o vsts-agent-linux-x64-3.248.0.tar.gz

mkdir myagent && cd myagent

tar zxvf ../vsts-agent-linux-x64-3.248.0.tar.gz
./config.sh

chmod +x ./bin/installdependencies.sh

./bin/installdependencies.sh

sudo ./bin/installdependencies.sh

sudo yum update -y

sudo rpm -Uvh https://packages.microsoft.com/config/centos/8/packages-microsoft-prod.rpm

sudo yum install -y dotnet-sdk-7.0
