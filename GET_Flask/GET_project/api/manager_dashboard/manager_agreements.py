from flask import Blueprint, request, jsonify, current_app
import datetime
from datetime import datetime, timedelta
from GET_project import db
from flask_jwt_extended import jwt_required
import io
from tempfile import TemporaryFile
from PIL import Image

GET_manager_agreements_Blueprint = Blueprint('GET_manager_agreements', __name__)
@GET_manager_agreements_Blueprint.route('/api/manager_dashboard/manager_agreements/', methods=['GET', 'POST']) # <- from '/'
@jwt_required()
def GET_manager_agreements():

    print('Home made it here --------------------------------------->')



    # investor_ID = request.json.get("investor_ID", None)
    # print('investor_ID: ', investor_ID)


    # NANO_FUND_ID = current_app.config['NANO_FUND_ID']

    # investor_info = db.investor_info.find_one({ "investor_ID": investor_ID },{"investments":1, "_id":0})
    # fund_info = db.fund_details.find({},{"fund_name":1, "fund_ID":1, "_id":0})

    # # funds = {}
    # # for fund in fund_info:
    # #     funds[fund['fund_ID']] = fund['fund_name']

    # legal_array = []
    # for fund in fund_info:
    #     fund_ID = fund['fund_ID']

    #     try:
    #         fund_name = investor_info['investments'][fund_ID]['fund_name']
    #         print(fund_name)
    #         iso_x = (investor_info['investments'][fund_ID]['datetime_signed']).strftime("%d/%m/%Y")
    #         print('x ----------------------- x')
    #         if fund_ID == NANO_FUND_ID:
    #             print('x ----------------------- fund_ID -   ', fund_ID)
    #             sub_agreement_url = '~/assets/legal/nano/Subscription_Agreement_&_Accredited_Cert__US_Nano_Fund_A.pdf'
    #             ppm_url = 'https://thisisget.com/legal_ag/nano/PPM_for_US_Nanotechnology_Fund_A.pdf'
    #             operating_url = 'https://thisisget.com/legal_ag/nano/US_Nano_Fund_A_Operating_Agreement.pdf'
    #             legal_array.append({'fund_name':fund_name, 'sub_agreement_url':sub_agreement_url, 'ppm_url':ppm_url, 'operating_url':operating_url})
    #     except:
    #         print('no_fund')

    # print(legal_array)

        
    # print(legal_array)



    #   file_list = []
    # for filename, file in request.files.items():
    #     print('test')
    #     file_list.append(filename)
    #     print(filename)
    #     print(file)
    # manager_ID = request.form['manager_ID']

    # print('manager_ID : ' + manager_ID)


    # user_info = db.credentials.find_one({ "user_id": manager_ID },{"dashboard_config":1})
    # current_profile_imgae = user_info['dashboard_config']['profile_img'] # <-- Image to be deleted


    # uploaded_document = request.files['file_1']
    # orig_image = Image.open(uploaded_document)
    # rgb_image = orig_image.convert('RGB')
    # new_width = 150
    # width, height = rgb_image.size   # Get dimensions
    # aspect_ratio = height / width
    # new_height = int(new_width * aspect_ratio)
    # resized_image = rgb_image.resize((new_width, new_height), Image.ANTIALIAS)


    # temp_file = TemporaryFile()
    # resized_image.save(temp_file, 'jpeg')
    # temp_file.seek(0)
    # resized = temp_file.read()

    
    # profile_uuid = str(uuid.uuid1())
    # db.credentials.update({"user_id": manager_ID}, {"$set": { 'dashboard_config': {'profile_img': profile_uuid}}})
    # fs = gridfs.GridFS(db)
    # fs.put(resized, filename=profile_uuid)
    # temp_file.close()


    # #delete old profile image
    # fs.delete(current_profile_imgae)

    # #send image back to client
    # profile_image = fs.get_last_version(profile_uuid)
    # base64_data = codecs.encode(profile_image.read(), 'base64')
    # profile_image = base64_data.decode('utf-8')


    return jsonify(
        table_data=[],
        message="Transfers fetched."
    ), 200


