#
# Open Live Departure Boards Web Service (OpenLDBWS) API Demonstrator Copyright (C)2018 OpenTrainTimes
# Ltd.
#
# This program is free software: you can redistribute it and/or modify it under the terms of the GNU
# General Public License as published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even
# the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General
# Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.  If not,
# see <https://www.gnu.org/licenses/>.
#
from zeep import Client
from zeep import xsd
from zeep import helpers
from zeep.plugins import HistoryPlugin
import sys
import json
import datetime
from api_key import LDB_TOKEN


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()

WSDL = 'http://lite.realtime.nationalrail.co.uk/OpenLDBWS/wsdl.aspx?ver=2017-10-01'
if LDB_TOKEN == '':
    raise Exception("Please configure your OpenLDBWS token in getDepartureBoardExample!")

history = HistoryPlugin()
client = Client(wsdl=WSDL, plugins=[history])
header = xsd.Element(
    '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}AccessToken',
    xsd.ComplexType([
        xsd.Element(
            '{http://thalesgroup.com/RTTI/2013-11-28/Token/types}TokenValue',
            xsd.String()),
    ])
)

header_value = header(TokenValue=LDB_TOKEN)
res = client.service.GetDepBoardWithDetails(numRows=10, crs='CLS', _soapheaders=[header_value])
input_dict = helpers.serialize_object(res)
db_as_str = json.dumps(input_dict, default=default)
services = res.trainServices.service
sys.stdout.write(db_as_str)
sys.stdout.flush()
sys.exit(0)


