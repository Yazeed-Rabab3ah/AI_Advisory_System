from rich.prompt import Prompt
from agno.agent import Agent
from agno.team import Team
from agno.models.openai import OpenAIResponses
import os
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb
from prompts import (
    TeamPrompt, LocationPrompt,
    CompetitorAnalysisPrompt, MenuPrompt, 
    PricePrompt, MarketingPrompt, 
    DeliveryPrompt, OperationsStaffingPrompt,
    LicensingPrompt, SupplierAgent,
    RiskPrompt,FinancialPrompt)
from agno.knowledge.knowledge import Knowledge
from agno.vectordb.chroma import ChromaDb
from agno.vectordb.search import SearchType
from agno.knowledge.embedder.openai import OpenAIEmbedder
from agno.tools.google.maps import GoogleMapTools
from agno.tools.duckduckgo import DuckDuckGoTools


load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')


locations_agent = Agent(
    name='Locations Agent',
    role=LocationPrompt.role,
    
    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),


    tools=[GoogleMapTools(
        key=os.getenv('GOOGLE_MAPS_API_KEY'),
        search_places=True,
    ),
    DuckDuckGoTools()],

    description=LocationPrompt.description,
    instructions=LocationPrompt.instructions,
    expected_output=LocationPrompt.expected_output,
    
)

competitors_analysis_agent = Agent(
    name='Competitor Analysis Agent',
    role='Analyze competitors in Dubai and Abu Dhabi for the restaurant expansion project.',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=CompetitorAnalysisPrompt.description,
    instructions=CompetitorAnalysisPrompt.instructions,
    expected_output=CompetitorAnalysisPrompt.expected_output,
)

menu_agent = Agent(
    name='Menu Strategy Agent',
    role='Design menu adaptations suitable for the UAE market for the restaurant expansion.',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=MenuPrompt.description,
    instructions=MenuPrompt.instructions,
    expected_output=MenuPrompt.expected_output,
)

pricing_agent = Agent(
    name='Pricing Strategy Agent',
    role='Recommend pricing ranges and positioning for the restaurant in Dubai and Abu Dhabi',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=PricePrompt.description,
    instructions=PricePrompt.instructions,
    expected_output=PricePrompt.expected_output,
)

marketing_agent = Agent(
    name='Marketing Strategy Agent',
    role='Design marketing and launch strategies for the restaurant expansion in Dubai and Abu Dhabi',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=MarketingPrompt.description,
    instructions=MarketingPrompt.instructions,
    expected_output=MarketingPrompt.expected_output,
)

delivery_agent = Agent(
    name='Delivery Platform Strategy Agent',
    role='Design delivery platform strategy for the restaurant expansion in Dubai and Abu Dhabi.',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=DeliveryPrompt.description,
    instructions=DeliveryPrompt.instructions,
    expected_output=DeliveryPrompt.expected_output,
)

operations_staffing_agent = Agent(
    name='Operations & Staffing Agent',
    role='Design operational structure and staffing plan for restaurant branches in Dubai and Abu Dhabi.',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=OperationsStaffingPrompt.description,
    instructions=OperationsStaffingPrompt.instructions,
    expected_output=OperationsStaffingPrompt.expected_output,
)

licensing_agent = Agent(
    name='Licensing & Regulatory Agent',
    role='Provide licensing and regulatory guidance for opening restaurant branches in Dubai and Abu Dhabi.',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=LicensingPrompt.description,
    instructions=LicensingPrompt.instructions,
    expected_output=LicensingPrompt.expected_output,
)

supplier_agent = Agent(
    name='Supplier Strategy Agent',
    role='Recommend supplier sourcing strategy for restaurant branches in Dubai and Abu Dhabi',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=SupplierAgent.description,
    instructions=SupplierAgent.instructions,
    expected_output=SupplierAgent.expected_output,
)

risk_agent = Agent(
    name='Risk Analysis Agent',
    role='Identify and analyze risks for opening restaurant branches in Dubai and Abu Dhabi',

    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=RiskPrompt.description,
    instructions=RiskPrompt.instructions,
    expected_output=RiskPrompt.expected_output,
)

financial_agent = Agent(
    name='Financial Analysis Agent',
    role='Analyze financial feasibility for opening restaurant branches in Dubai and Abu Dhabi',
    
    model=OpenAIResponses(id='gpt-4.1-mini-2025-04-14', api_key=api_key),

    tools=[DuckDuckGoTools()],

    description=FinancialPrompt.description,
    instructions=FinancialPrompt.instructions,
    expected_output=FinancialPrompt.expected_output
)




knowledge = Knowledge(
    name = "Company local data in Jordan",
    description = "Internal dataset about a restaurant business in Jordan, including company background, branches, employees, salaries, suppliers, operations, competitors, and financial data for analysis and decision-making.",
    vector_db=ChromaDb(
        collection='docs',
        path='chromadb',
        persistent_client=True,
        search_type=SearchType.hybrid,
        embedder=OpenAIEmbedder(id='text-embedding-3-small', api_key=os.getenv('OPENAI_API_KEY'))
    )
)

knowledge.insert(path='docs/company_data.pdf')




master = Team(
    members=[locations_agent, competitors_analysis_agent,
            menu_agent, pricing_agent, marketing_agent, 
            delivery_agent, operations_staffing_agent,
            licensing_agent, supplier_agent, risk_agent,
            financial_agent, ],
    name='Intelligent Market Expansion Advisor',
    role='Helping Jordanian local restaurant expanding to UAE',

    model=OpenAIResponses(id='gpt-4.1-2025-04-14', api_key=os.getenv('OPENAI_API_KEY')),

    description=TeamPrompt.description,
    instructions=TeamPrompt.instructions,
    expected_output= TeamPrompt.expected_output,

    knowledge=knowledge,

    db=SqliteDb(db_file='data.db'),
    
    add_history_to_context=True,
    num_history_runs=3,
    

    markdown=True,
    stream=True,
)


if __name__ == "__main__":
    
    while True:
        user_input = Prompt.ask('User')

        if user_input == 'exit':
            break

        master.print_response(user_input, stream=True)
        
