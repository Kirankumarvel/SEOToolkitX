import os
from google.ads.googleads.client import GoogleAdsClient
from google.ads.googleads.errors import GoogleAdsException
import pandas as pd
from dotenv import load_dotenv

# Load environment variables (API keys)
load_dotenv()

def fetch_keyword_ideas(keyword, location_id="2840"):  # 2840 = USA
    try:
        # Initialize Google Ads client
        googleads_client = GoogleAdsClient.load_from_env()

        # Request keyword ideas
        keyword_plan_idea_service = googleads_client.get_service("KeywordPlanIdeaService")
        request = googleads_client.get_type("GenerateKeywordIdeasRequest")
        request.customer_id = os.getenv("GOOGLE_ADS_CUSTOMER_ID")
        request.language = "en"
        request.geo_target_constants = [f"geoTargetConstants/{location_id}"]
        request.keyword_seed.keywords.extend([keyword])

        # Fetch results
        response = keyword_plan_idea_service.generate_keyword_ideas(request=request)
        
        # Parse results into a DataFrame
        keywords_data = []
        for idea in response:
            keywords_data.append({
                "Keyword": idea.text,
                "Avg. Monthly Searches": idea.keyword_idea_metrics.avg_monthly_searches,
                "Competition": idea.keyword_idea_metrics.competition.name,
            })

        return pd.DataFrame(keywords_data)

    except GoogleAdsException as ex:
        print(f"Google Ads API error: {ex}")
        return pd.DataFrame()

if __name__ == "__main__":
    # Example usage
    df = fetch_keyword_ideas("best running shoes")
    if not df.empty:
        print(df.head())
        df.to_csv("keyword_results.csv", index=False)
