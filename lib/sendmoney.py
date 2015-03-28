import requests, random
import xml.etree.ElementTree as ET

class SendMoney():
  def __init__(self):
    self._mapping_url = "http://dmartin.org:8028/moneysend/v2/mapping/card?Format=XML"
    self._transfer_url = "http://dmartin.org:8028/moneysend/v2/transfer?Format=XML"

  def generate_mapping_xml(self, phone_number, card_number, expiry):
    el_create_mapping_request = ET.Element('CreateMappingRequest')
    el_subscriber_id = ET.SubElement(el_create_mapping_request, 'SubscriberId')
    el_subscriber_id.text = phone_number
    el_subscriber_type = ET.SubElement(el_create_mapping_request, 'SubscriberType')
    el_subscriber_type.text = "PHONE_NUMBER"
    el_account_usage = ET.SubElement(el_create_mapping_request, 'AccountUsage')
    el_account_usage.text = "RECEIVING"
    el_default_indicator = ET.SubElement(el_create_mapping_request, 'DefaultIndicator')
    el_default_indicator.text = "T"
    el_alias = ET.SubElement(el_create_mapping_request, 'Alias')
    el_alias.text = "TELLER CARD"
    el_ica = ET.SubElement(el_create_mapping_request, 'ICA')
    el_ica.text = "009674"
    el_account_number = ET.SubElement(el_create_mapping_request, 'AccountNumber')
    el_account_number.text = card_number
    el_expiry_date = ET.SubElement(el_create_mapping_request, 'ExpiryDate')
    el_expiry_date.text = expiry
    el_cardholder_full_name = ET.SubElement(el_create_mapping_request, 'CardholderFullName')
    el_cardholder_first_name = ET.SubElement(el_cardholder_full_name, 'CardholderFirstName')
    el_cardholder_first_name.text = "FIRST"
    el_cardholder_middle_name = ET.SubElement(el_cardholder_full_name, 'CardholderMiddleName')
    el_cardholder_middle_name.text = "M"
    el_cardholder_last_name = ET.SubElement(el_cardholder_full_name, 'CardholderLastName')
    el_cardholder_last_name.text = "LAST"
    el_address = ET.SubElement(el_create_mapping_request, 'Address')
    el_line1 = ET.SubElement(el_address, 'Line1')
    el_line1.text = "ADDRESS LINE 1"
    el_line2 = ET.SubElement(el_address, 'Line2')
    el_line2.text = "ADDRESS LINE 2"
    el_city = ET.SubElement(el_address, 'City')
    el_city.text = "CITY"
    el_country_subdivision = ET.SubElement(el_address, 'CountrySubdivision')
    el_country_subdivision.text = "MO"
    el_postal_code = ET.SubElement(el_address, 'PostalCode')
    el_postal_code.text = "POSTALCODE"
    el_country = ET.SubElement(el_address, 'Country')
    el_country.text = "USA"
    el_date_of_birth = ET.SubElement(el_create_mapping_request, 'DateOfBirth')
    el_date_of_birth.text = "19460102"
    return ET.tostring(el_create_mapping_request)

  def generate_mapping_response_xml(xml_response):
    create_mapping = createmapping.CreateMapping()
    create_mapping.request_id = xml_response.find('RequestId').text
    tmp_mapping = mapping.Mapping()
    tmp_mapping.mapping_id = xml_response.find('Mapping/MappingId').text
    create_mapping.mapping = tmp_mapping
    return create_mapping


  def setup_phone(self, phone_number, credit_card_number, expiry):
    """takes a phone number and credit card and links them via mapping"""
    card = "5184680430000006"
    exp = "201401"
    xml = self.generate_mapping_xml(phone_number, card, exp)
    print xml
    headers = {'Content-Type': 'application/xml'}
    r = requests.post(self._mapping_url, data=xml, headers=headers)
    print r.text

  def transfer_request(self):
    print("yeah, bitch!")
