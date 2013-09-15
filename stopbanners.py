from yapi import * 
 
token = 'ac6f9f91c3754ea49a6f65f432627b2a'
client = YandexApiService(token)
 
campaigns = client.query('GetCampaignsList')

even_campaign_ids = []
for campaign in campaigns:
    if campaign['CampaignID'] % 2 == 0:
        even_campaign_ids.append(campaign['CampaignID'])
        
banners = client.query('GetBanners', {'CampaignIDS': even_campaign_ids})
 
uneven_banner_ids = []
for banner in banners:
    if banner['BannerID'] % 2 != 0:
        uneven_banner_ids.append(banner['BannerID'])

print uneven_banner_ids         
client.query('StopBanners', {'BannerIDS': uneven_banner_ids})
