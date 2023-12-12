text_snippets = [
    "Few years ago Mustang district is the best place for trekking by foot or riding horse. After road construction there are many possibilities arise like tours, biking and other things to do in Mustang Nepal. Now it is easy to experience the ancient culture by trekking, tours, biking, and horse riding which remains unchanged for decades.",
    "What are the best things to do in Mustang Nepal? Exciting things to do in Mustang Nepal are listed below for reference to the travelers. It helps them to prepare mentally; what to do during upcoming upper mustang trip in advance.",
    "16: Take pictures of landscape, wildlife, and Himalayan settlements Taking Selfi is a part of travel these days to keep memory alive forever. It is good to capture some more events picture and videos of upper mustang. Dramatic landscape, wildlife, sky tombs Nepal, High Mountain and Himalayan settlements are the major attraction to capture on camera. Collecting the pictures of this dream land is another popular thing to experience in Mustang Nepal.",
    "There are many things to perform in Nepal such as adventurous sport like trekking, mountain biking, royal Enfield tours, jeep safari and more. Expert guide lead you and provide a helping hand even in the high cliffs. Lo Manthang is a place where you can find top things to do in Mustang Nepal.",
    "Mustang Nepal is a beautiful and unique region that is well worth a visit. From trekking to Lo Manthang to exploring the ancient caves, there are plenty of things to see and do in Mustang. If you are looking for an adventure that is off the beaten path, then Mustang is the perfect destination.",
    "Hopefully; you are clear to prepare mentally, what are the things to do in Mustang Nepal. If you have any suggestion, comment, recommendation, or any inquiry related with, do not hesitate to contact us."
]

# Keywords for filtering
keywords = ["Weather", "View","Mountain","Nature","Beautiful"]

# Filter content related to specified keywords
related_content = [snippet for snippet in text_snippets if any(keyword in snippet for keyword in keywords)]

# Print the filtered content
for idx, content in enumerate(related_content, start=1):
    print(f"Related content {idx}:")
    print(content)
    print("-" * 50)  # Separator for clarity
