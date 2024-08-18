# import os
# import django

# # Set the DJANGO_SETTINGS_MODULE environment variable
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btre.settings")
# django.setup()


# from listings.models import HotelRoom, Listing, RentHouse
# from realtors.models import Realtor 

# lst = [Listing, RentHouse]

# rea = Realtor.objects.get(id=23)

# # for item in lst:
# #     new_item = item.objects.create(
# #         realtor=rea,
# #         title='AB Goldphase',
# #         address='Gorantla',
# #         city='Guntur',
# #         state='AP',
# #         zipcode='522001',
# #         description='''Stunning independent house villa for sale in ab goldphase, gorantla, guntur, a p


# # Introducing a magnificent independent house villa nestled in a prime location of gorantla, guntur. This exquisite property offers luxurious living combined with contemporary design and an array of desirable features. Ideal for those seeking a serene and upscale lifestyle, this villa is a true gem in the heart of the city.
# # Key features:
# # Spacious layout: You will love this villa, constructed on a plot area of 1596sq. Ft. This independent house villa boasts a generous floor plan, with 3 bedrooms and 4 bathrooms, 2 balcony with a pooja room. The well-Designed layout offers a seamless flow between rooms and a perfect balance of privacy and togetherness. The villa is an unfurnished unit and awaits your personal touch.
# # Gourmet kitchen: The villa features a fully-Equipped gourmet kitchen with ample storage space, and a convenient layout, so preparing meals becomes a pleasure.
# # Private outdoor space: Enjoy the beauty of nature and relax in the tranquility of your own private outdoor oasis. The villa offers a well-Manicured garden and a spacious patio or terrace area, ideal for hosting gatherings or simply unwinding amidst the scenic surroundings.
# # Amenities:
# # Feng shui / vaastu compliant, private garden / terrace, water storage, visitor parking, swimming pool, gymnasium.Clubhouse,24/7 security, dedicated parking, children's play area, jogging track land, scaped gardens
# # Location:
# # This independent house villa enjoys a coveted location in mangalore. Situated in a prestigious neighborhood, it provides convenient access to major landmarks, schools, hospitals, shopping centers, etc. Residents can take advantage of the excellent connectivity and proximity to essential amenities, ensuring a comfortable and convenient lifestyle.
# # Wait no more and schedule a tour today.
# # For more information, kindly contact the owner.''',
# #         contact_info=66123456789,
# #         price=8700000,
# #         bedrooms=3,
# #         bathrooms=4,
# #         garage=1,
# #         sqft=1596,

# #         photo_main=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Simple-Modern-House-Design-Plan10-x-10-meters-with-3-Bedrooms-1.jpg",
# #         photo_1=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Screenshot 2023-11-11 230701.png",
# #         photo_2=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Screenshot 2023-11-11 230832.png",
# #         photo_3=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Screenshot 2023-11-11 230932.png"
# #     )
# #     new_item.save()
# #     print('DONE!')


# hotel = HotelRoom.objects.create(
#     realtor=rea,
#     title='Hotel Southern Grand',
#     address='Office 26, 6-8, Papaiah St, opp. Sub Registration, Near Thaluka, Gandhi Nagar, Vijayawada, Andhra Pradesh 520003',
#     city='Vijayawada',
#     state='AP',
#     zipcode='520003',
#     description='''This relaxed hotel is a 9-minute walk from Vijayawada Junction train station, 7 km from the ancient temples in Undavalli Caves and 20 km from Vijayawada International Airport.
# The warm, unfussy rooms provide free Wi-Fi, flat-screen TVs and minibars, plus tea and coffeemaking facilities. Room service is available 24/7, and children age 5 and under stay at no extra charge.
# Freebies include breakfast, parking, and transportation from the airport or train station. There's a casual vegetarian restaurant and a conference hall.''',

#     embed_lnk='<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d244811.61117004303!2d80.44335301290087!3d16.516936!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3a35ef7e6c8b7d49%3A0xcac2d392e9e8225f!2sHotel%20Southern%20Grand%2C%20Vijayawada!5e0!3m2!1sen!2sin!4v1699863098615!5m2!1sen!2sin" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>',
#     contact_information=66987654321,
#     price=1870,
#     room_size=370,
#     no_of_beds=1,
#     bed_type='king',
#     num_bathrooms=1,
#     has_air_conditioned=True,
#     has_wifi=True,
#     has_pool=False,
#     has_restaurant=True,
#     has_tv=True,
#     photo_main=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Screenshot 2023-11-11 225714.png",
#     photo_1=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Screenshot 2023-11-11 230701.png",
#     photo_2=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Screenshot 2023-11-11 230832.png",
#     photo_3=r"C:\Users\modhe\Desktop\btre_project-master\media\photos\pics\Screenshot 2023-11-11 230932.png"
#     )
# print('Done')