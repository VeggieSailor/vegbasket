from django.core.files.base import ContentFile
from requests import request, ConnectionError


def save_profile(backend, user, response, is_new,  *args, **kwargs):
    '''
    Get the user avatar (and any other details you're interested in)
    and save them to the userprofile
    '''
    if backend.name == 'google-plus':  
        if response.get('image') and response['image'].get('url'):
            url = response['image'].get('url')
            prof = user.userprofile
            if prof.avatar:
                # if existing avatar stick with it rather than google syncing
                pass
            else:
                try:
                    response = request('GET', url)
                    response.raise_for_status()
                except ConnectionError:
                    pass
                else:
                    # No avatar so sync it with the google one.
                    # Passing '' for name will invoke my upload_to function
                    # saving by username (you prob want to change this!)
                    prof.avatar.save(u'%s.jpg' % user.id,
                                    ContentFile(response.content),
                                    save=False
                                    )
                    prof.save()
    elif backend.name == 'facebook':   # and is_new:
        prof = user.userprofile
        if prof.avatar:
            pass
        else:
            url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])

            try:
                response = request('GET', url, params={'type': 'large'})
                response.raise_for_status()
            except ConnectionError:
                pass
            else:
                prof.avatar.save(u'%s.jpg' % user.id,
                                 ContentFile(response.content),
                                 save=False
                                 )
                prof.save()
    elif backend.name == 'vk-oauth2':  
        if response.get('photo'):
            url = response['photo']
            prof = user.userprofile
            if prof.avatar:
                # if existing avatar stick with it rather than google syncing
                pass
            else:
                try:
                    response = request('GET', url)
                    response.raise_for_status()
                except ConnectionError:
                    pass
                else:
                    # No avatar so sync it with the google one.
                    # Passing '' for name will invoke my upload_to function
                    # saving by username (you prob want to change this!)
                    prof.avatar.save(u'%s.jpg' % user.id,
                                    ContentFile(response.content),
                                    save=False
                                    )
                    prof.save()                
    else:  
        url = 'http://api.adorable.io/avatars/%s/test.png' % user.id
        prof = user.userprofile
        if prof.avatar:
            # if existing avatar stick with it rather than google syncing
            pass
        else:
            try:
                response = request('GET', url)
                response.raise_for_status()
            except ConnectionError:
                pass
            else:
                # No avatar so sync it with the google one.
                # Passing '' for name will invoke my upload_to function
                # saving by username (you prob want to change this!)
                prof.avatar.save(u'%s.png' % user.id,
                                ContentFile(response.content),
                                save=False
                                )
                prof.save()    
            
                
                
                