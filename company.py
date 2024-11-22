from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from api.v1.endpoints.models.company_model import CompanyModel
from models.company import Company
from database import get_db

router = APIRouter(prefix="/persimmon", tags=["Company Details"])

@router.get("/company/get/{company_id}")
async def get_company_by_id(company_id: int, session : Session = Depends(get_db)):
    try:
        db_company = Company.get_by_id(company_id=company_id, session= session)

        if not db_company:
            raise HTTPException(status_code=404, detail="Company not found with id '{company_id}'")
        
        return {
                "id": db_company.id,
                "name": db_company.name,
                "website": db_company.website,
                "number_of_employees": db_company.number_of_employees,
                "industry_type": db_company.industry_type,
                "linkedin": db_company.linkedin,
                "type": db_company.type.name
        }
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/company/get")
async def get_all_company(page:int = 1, page_size: int = 20, session : Session = Depends(get_db)):
    try:
        response = Company.get_all(page=page, page_size=page_size, session=session)
        # db_companys = Company.get_all(session=session)
        # if not db_companys:
        #     raise HTTPException(status_code=404, detail="Company not found with id '{company_id}'")
        
        # companies = []

        # for db_company in db_companys:
        #     company = {
        #         "id": db_company.id,
        #         "name": db_company.name,
        #         "website": db_company.website,
        #         "number_of_employees": db_company.number_of_employees,
        #         "industry_type": db_company.industry_type,
        #         "linkedin": db_company.linkedin,
        #         "type": db_company.type.name
        #     }
        #     companies.append(company)

        companies = []
        for db_company in response['companies']:
            company = {
                "id": db_company.id,
                "name": db_company.name,
                "website": db_company.website,
                "number_of_employees": db_company.number_of_employees,
                "industry_type": db_company.industry_type,
                "linkedin": db_company.linkedin,
                "type": db_company.type.name
            }
            companies.append(company)
        response['companies'] = companies
        response['status'] = status.HTTP_200_OK
        return response
    
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))    


@router.post("/company")
async def create_company(company: CompanyModel, session : Session = Depends(get_db)):
    try:
        db_company = Company(
            name =company.name,
            website = company.website,
            number_of_employees= company.number_of_employees,
            industry_type= company.industry_type,
            linkedin= company.linkedin,
            type= company.type.name
        )
        return db_company.create(session=session)

    except Exception as e:
        print(f"Error occured : {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    


@router.put("/company/{company_id}")
async def update_company(company_id: int, company: CompanyModel, session: Session = Depends(get_db)):
    try:
        db_company = Company.get_by_id(session=session, company_id=company_id)
        if not db_company:
            raise HTTPException(status_code=404, detail="Company not found with id '{company_id}'")
        db_company.name =company.name,
        db_company.website = company.website,
        db_company.number_of_employees= company.number_of_employees,
        db_company.industry_type= company.industry_type,
        db_company.linkedin= company.linkedin,
        db_company.type= company.type.name

        company =  db_company.update(session= session)
        return {
            "id": db_company.id,
            "name": db_company.name,
            "website": db_company.website,
            "number_of_employees": db_company.number_of_employees,
            "industry_type": db_company.industry_type,
            "linkedin": db_company.linkedin,
            "type": db_company.type.name
        }
    
    except Exception as e:
        print(f"Error occured : {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    


@router.delete("company/{company_id}")
async def delete(company_id: int, session:Session = Depends(get_db)):
    return Company.delete(company_id=company_id, session=session)
    