# Tools needed

Install at least Java 8

```bash
sudo apt-get install openjdk-8-jre
```

download the latest swagger-codegen
```bash
wget https://repo1.maven.org/maven2/io/swagger/swagger-codegen-cli/2.4.14/swagger-codegen-cli-2.4.14.jar
```

Review the config parameters
```bash
java -jar swagger-codegen-cli-2.4.14.jar config-help -l python
```

Create a config json file ipamsvc.json

```json
{
    "packageName":"ibcsp_ipamsvc",
    "projectName":"ibcsp-ipamsvc",
    "packageVersion":"0.0.1"
}
```

Generate the Code

```bash
java -jar swagger-codegen-cli-2.4.14.jar generate -c ipamsvc.json -i https://csp.infoblox.com/apidoc/docs/Ipamsvc -l python -o /home/git.metrosystems.net/ibcsp_ipamsvc/
```