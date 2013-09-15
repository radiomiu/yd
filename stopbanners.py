from yapi import * 
 
token = 'ac6f9f91c3754ea49a6f65f432627b2a'
client = YandexApiService(token)
 
campaigns = client.query('GetCampaignsList')
activecampaigns =  client.query('GetCampaignsListFilter', {'Filter':{'IsActive': ['Yes']}})
 
even_campaign_ids = []
grouped_odd_banners = {} 
 
for campaign in activecampaigns:
    campaign_id = campaign['CampaignID']
    if campaign_id % 2 == 0:
        grouped_odd_banners[campaign_id] = []
        even_campaign_ids.append(campaign_id)
        
banners = client.query('GetBanners', {'CampaignIDS': even_campaign_ids})
 
for banner in banners:
    banner_id = banner['BannerID']
    if banner_id % 2 != 0:
        grouped_odd_banners[banner['CampaignID']].append(banner_id)
 
for campaign_id, odd_banner_ids in grouped_odd_banners.iteritems():
    client.query('ResumeBanners', {'CampaignID': campaign_id, 'BannerIDS': odd_banner_ids})
    print odd_banner_ids
