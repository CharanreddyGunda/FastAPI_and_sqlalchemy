from pydantic import BaseModel, field_validator
import re

from api.v1.validator import is_non_empty, validate_length
from models.company import CompanyTypeEnum

COMPANY_NAME_FIELD = "company name"
COMPANY_WEBSITE_FIELD = "website url"
NUMBER_OF_EMPLOYEES = "number of employees"
INDUSTRY_TYPE = "industry type"
LINKEDIN_URL = "linkedin url"
TYPE = "company type"


class CompanyModel(BaseModel):
    name: str
    website: str
    number_of_employees: str
    industry_type: str
    linkedin: str
    type: CompanyTypeEnum

    @field_validator('name')
    def validate_name(cls, name):
        is_non_empty(value=name, field_name=COMPANY_NAME_FIELD)
        validate_length(value=name, min_len=3, max_len=50, field_name=COMPANY_NAME_FIELD)
        if not re.match(r'^[a-zA-Z0-9&\-\.\'\s]+$', name):
            raise ValueError("Company name can only contain alphanumeric characters, spaces, &, -, ., and '")
        return name

    @field_validator('website')
    def validate_website(cls, website):
        is_non_empty(value=website, field_name=COMPANY_WEBSITE_FIELD)
        validate_length(value=website, min_len=10 , max_len=100, field_name=COMPANY_WEBSITE_FIELD)
        return website
    
    # @field_validator('number_of_employees')
    # def validate_number_of_employees(cls, number_of_employees):
    #     is_non_empty(value=number_of_employees, field_name=NUMBER_OF_EMPLOYEES)

    # @field_validator('industry_type')
    # def validate_industry_type(cls, industry_type):
    #     is_non_empty(value=industry_type, field_name=INDUSTRY_TYPE)

    # @field_validator('linkedin')
    # def validate_linkedin(cls, linkedin):
    #     is_non_empty(value=linkedin, field_name=LINKEDIN_URL)


    


    

    