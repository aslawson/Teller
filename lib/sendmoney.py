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
    el_account_usage.text = "SEND_RECV"
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

  def generate_transaction_xml(self, sender_phone, receiver_phone, amount):
    amount = str(amount)
    random19 = ''.join(str(random.randint(0,9)) for _ in xrange(19))
    random3 = ''.join(str(random.randint(0,7)) for _ in xrange(3))

    el_transfer_request = ET.Element('TransferRequest')
    el_local_date = ET.SubElement(el_transfer_request, 'LocalDate')
    el_local_date.text = "0612"
    el_local_time = ET.SubElement(el_transfer_request, 'LocalTime')
    el_local_time.text = "161"+str(random3)
    el_transaction_reference = ET.SubElement(el_transfer_request, 'TransactionReference')
    el_transaction_reference.text = random19;

    el_funding_mapped = ET.SubElement(el_transfer_request, 'FundingMapped')
    el_subscriber_id = ET.SubElement(el_funding_mapped, 'SubscriberId')
    el_subscriber_id.text = sender_phone
    el_subscriber_type = ET.SubElement(el_funding_mapped, 'SubscriberType')
    el_subscriber_type.text = "PHONE_NUMBER"
    el_subscriber_alias = ET.SubElement(el_funding_mapped, 'SubscriberAlias')
    el_subscriber_alias.text = "TELLER CARD"

    el_funding_amount = ET.SubElement(el_transfer_request, 'FundingAmount')
    el_receiving_value = ET.SubElement(el_funding_amount, 'Value')
    el_receiving_value.text = amount
    el_receiving_currency = ET.SubElement(el_funding_amount, 'Currency')
    el_receiving_currency.text = "702"

    el_receiving_mapped = ET.SubElement(el_transfer_request, 'ReceivingMapped')
    el_subscriber_id = ET.SubElement(el_receiving_mapped, 'SubscriberId')
    el_subscriber_id.text = receiver_phone
    el_subscriber_type = ET.SubElement(el_receiving_mapped, 'SubscriberType')
    el_subscriber_type.text = "PHONE_NUMBER"
    el_subscriber_alias = ET.SubElement(el_receiving_mapped, 'SubscriberAlias')
    el_subscriber_alias.text = "TELLER CARD"

    el_receiving_amount = ET.SubElement(el_transfer_request, 'ReceivingAmount')
    el_receiving_value = ET.SubElement(el_receiving_amount, 'Value')
    el_receiving_value.text = amount
    el_receiving_currency = ET.SubElement(el_receiving_amount, 'Currency')
    el_receiving_currency.text = "702"

    el_channel = ET.SubElement(el_transfer_request, 'Channel')
    el_channel.text = "W"
    el_ucaf_support = ET.SubElement(el_transfer_request, 'UCAFSupport')
    el_ucaf_support.text = "true"
    el_ica = ET.SubElement(el_transfer_request, 'ICA')
    el_ica.text = "009674"
    el_processor_id = ET.SubElement(el_transfer_request, 'ProcessorId')
    el_processor_id.text = "9000000442"
    el_routing_and_transit_number = ET.SubElement(el_transfer_request, 'RoutingAndTransitNumber')
    el_routing_and_transit_number.text = "990442082"
    el_card_acceptor = ET.SubElement(el_transfer_request, 'CardAcceptor')
    el_acceptor_name = ET.SubElement(el_card_acceptor, 'Name')
    el_acceptor_name.text = "My Local Bank"
    el_acceptor_city = ET.SubElement(el_card_acceptor, 'City')
    el_acceptor_city.text = "Saint Louis"
    el_acceptor_state = ET.SubElement(el_card_acceptor, 'State')
    el_acceptor_state.text = "MO"
    el_acceptor_postal_code = ET.SubElement(el_card_acceptor, 'PostalCode')
    el_acceptor_postal_code.text = "63101"
    el_acceptor_country = ET.SubElement(el_card_acceptor, 'Country')
    el_acceptor_country.text = "USA"
    el_transaction_desc = ET.SubElement(el_transfer_request, 'TransactionDesc')
    el_transaction_desc.text = "P2P"
    el_merchant_id = ET.SubElement(el_transfer_request, 'MerchantId')
    el_merchant_id.text = "123456"
    return ET.tostring(el_transfer_request)

  def setup_phone(self, phone_number, credit_card_number, expiry):
    """takes a phone number and credit card and links them via mapping"""
    xml = self.generate_mapping_xml(phone_number, credit_card_number, expiry)
    headers = {'Content-Type': 'application/xml'}
    r = requests.post(self._mapping_url, data=xml, headers=headers)
    print "\n", r.text, "\n"

  def transfer_request(self, sender_phone, receiver_phone, amount):
    xml2 = self.generate_transaction_xml(sender_phone, receiver_phone, amount)
    headers = {'Content-Type': 'application/xml'}
    r = requests.post(self._transfer_url, data=xml2, headers=headers)
    print xml2
    print r.text
