import os
from market_analysis.team_leader import MarketAnalysisTeamLeader
from risk_management.team_leader import RiskManagementTeamLeader
from trading_execution.team_leader import TradingExecutionTeamLeader

def main():
    # Initialize team leaders
    market_analysis_leader = MarketAnalysisTeamLeader()
    risk_management_leader = RiskManagementTeamLeader()
    trading_execution_leader = TradingExecutionTeamLeader()

    # Run team leaders
    market_analysis_leader.run()
    risk_management_leader.run()
    trading_execution_leader.run()

if __name__ == "__main__":
    main()
