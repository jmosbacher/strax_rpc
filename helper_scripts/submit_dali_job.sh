#!/bin/bash
#SBATCH --job-name=straxui
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=4480

#SBATCH --time=24:00:00

#SBATCH --account=pi-lgrandi
#SBATCH --partition=dali
#SBATCH --qos=dali

#SBATCH --output=straxui/straxui-log-%J.txt
#SBATCH --error=straxui/straxui-log-%J.txt

# Put your desired root directory here, must contain the straxui folder
cd /home/mosbacher

export PATH=/home/mosbacher/anaconda3/bin:$PATH

#### Start up a straxrpc server ####

# source activate strax_test
source /dali/lgrandi/tunnell/s3_osg.sh
python ./straxui/run_straxrpc_server.py &

#### Start up a straxui server ####

export BOKEH_SECRET_KEY=$(bokeh secret)
export BOKEH_SIGN_SESSIONS=true
ipnport=$(shuf -i8000-9999 -n1)
ipnip=$(hostname -i)
sessionid1=$(python ./straxui/gen_session.py)
sessionid2=$(python ./straxui/gen_session.py)
sessionid3=$(python ./straxui/gen_session.py)

echo -e "
    Copy/Paste this in your local terminal to ssh tunnel with remote
    ----------------------------------------------------------------------------
    ssh -N -f -L $ipnport:$ipnip:$ipnport ${USER}@midway2.rcc.uchicago.edu
    ----------------------------------------------------------------------------

    Then open a browser on your local machine to one of the following addresses:
    ----------------------------------------------------------------------------
    localhost:$ipnport/straxui?bokeh-session-id=$sessionid1
    localhost:$ipnport/straxui?bokeh-session-id=$sessionid2
    localhost:$ipnport/straxui?bokeh-session-id=$sessionid3
    ----------------------------------------------------------------------------
    You can also sign a new session id using the secret key for this session:
    $BOKEH_SECRET_KEY
    This key will only be valid for this job.
    "

bokeh serve straxui --port=$ipnport --address=$ipnip --allow-websocket-origin=* --session-ids external-signed