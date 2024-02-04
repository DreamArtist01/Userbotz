# (c) @PremiumBotz https://telegram.me/premiumbotz
import os


class Config(object):
    API_ID = int(os.environ.get('APP_ID', 28263171))
    API_HASH = os.environ.get('API_HASH', "d56ea958bcb261d7c39c518b495ee392")
    SESSION_STRING = os.environ.get('SESSION_STRING', "BQFAayoAYOpADhLflog-haBdK6Y6Vv0TK5OVZVpM-vwy8Igky7NdR1voDY7mBCBlUAmyJbOjPb5pfT--OofBiQS2zT5t2LPl_pHXqX5_s3h-0BEwq219g0ek5PObLao8kgx4rgYa42jCZ9oWFifUBvaYqXxa_g1TlrV3fXBFA8MvypGeO-3fm6WY4DselY_v6lS4rpnKGvC2rExazaDRA6DJNc2lp6YQ30_j7WfiatlT727ph8AlHqe7myYbGJ1gB0Kou8L7DW2RptbPvSmHkdOfzQSDspNlekQfXBVJpQLJzaO30LrEQSbTGf8jT6n1hV68HgD9SRVClBDf5XklE3ALZqWwEgAAAAGRKY04AA")
    target_groups = os.environ.get('target_groups', "adult_girls_chatting_groupp and_girls_and_boys_chatting And_Girls_Boys_Chatting_Group_1 indian_girls_chattingg_groupz girls_Love_chatting_group_07 Cum_Tribute_WORLLD adult_chatting_group_official Wife_Swapping_Indiaa_group indian_girls_chatting_groupx adult_chattingg_group And_Girls_Boys_Group_Chatting indians_girls_chattingg_group girls_Love_chatting_group_07 mallu_chat_cucks_1 WIFE_SWAPPING_INDIA_REAL")
    TARGET_GROUPS = list(set([x for x in target_groups.split()]))
    MESSAGE1 = os.environ.get('MESSAGE1', "Abhi Free hu, Come Baby ❤️")
    MESSAGE2 = os.environ.get('MESSAGE2', "Handsome Boy, DM me ❣️")
    MESSAGE3 = os.environ.get('MESSAGE3', "Come For Naughty Fun 💋")
    MESSAGE4 = os.environ.get('MESSAGE4', "Aao fun kare")
    MESSAGE5 = os.environ.get('MESSAGE5', "Mood me hu boys")