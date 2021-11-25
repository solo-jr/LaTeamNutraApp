#!/bin/bash
venv_python=/home/inst-la-team-nutra-app/envronment_dir/venv/ltn_p3.7/bin/python
bin_odoo=/home/inst-la-team-nutra-app/envronment_dir/ressources/git/kernel/odoo/odoo-bin
conf_odoo=/home/inst-la-team-nutra-app/envronment_dir/ressources/conf_local/app.lateamnutra.com.conf
parms_odoo="-c $conf_odoo"
database_init=""
app_update_init=""
get_conf ()
{
	val=`cat $conf_odoo | grep -e ^$1 | cut -d = -f 2`
	val_clean=${val##" "}
	echo "$val_clean"
}

database_init=`get_conf database_init`
app_update_init=`get_conf app_update_init`

if [ ! $database_init = "" ] && [ ! $app_update_init = "" ]
then
	parms_odoo="$parms_odoo -d $database_init -u $app_update_init"
fi
final_script="$venv_python $bin_odoo $parms_odoo"
$final_script

