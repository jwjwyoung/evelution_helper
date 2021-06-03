# Q 0 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 1 : # @message.plaintext_body
Query(Message)

# Q 2 : # @invitation_request.email
Query(InvitationRequest)
.select('email')
# Q 3 : # @comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 4 : # @comment.user
Query(User)
.where("id = ?")
# Q 5 : # @comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 6 : # @comment.user
Query(User)
.where("id = ?")
# Q 7 : # @invitation.email
Query(Invitation)
.select('email')
# Q 8 : # story.short_id
Query(Story)
.select('short_id')
# Q 9 : # story.short_id
Query(Story)
.select('short_id')
# Q 10 : # @user.email
Query(User)
.select('email')
# Q 11 : # comment.persisted?
Query(Comment)

# Q 12 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 13 : # @comments.each
Query(Comment)

# Q 14 : # story.vote
Query(Story)

# Q 15 : # story.vote
Query(Story)

# Q 16 : # comment.score
Query(Comment)

# Q 17 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 18 : # @user.id
Query(User)

# Q 19 : # @message.url
Query(Message)

# Q 20 : # @user.username
Query(User)
.select('username')
# Q 21 : # @invitation_request.ip_address
Query(InvitationRequest)
.select('ip_address')
# Q 22 : # @comment.plaintext_comment
Query(Comment)

# Q 23 : # @comment.plaintext_comment
Query(Comment)

# Q 24 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 25 : # @invitation.user
Query(User)
.where("id = ?")
# Q 26 : # @invitation.memo.present?
Query(Invitation)
.select('memo')
# Q 27 : # @invitation.memo
Query(Invitation)
.select('memo')
# Q 28 : # @invitation.memo
Query(Invitation)
.select('memo')
# Q 29 : # story.vote
Query(Story)

# Q 30 : # story.vote
Query(Story)

# Q 31 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 32 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 33 : # story.score
Query(Story)

# Q 34 : # User.where(:username => params[:username]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 35 : # User.where(:username => params[:username]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 36 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 37 : # User.where(:username => params[:username]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 38 : # User.make!(:username => nil)
Query(User)

# Q 39 : # User.make!
Query(User)

# Q 40 : # User.make!(:username => nil)
Query(User)

# Q 41 : # User.make!
Query(User)

# Q 42 : # User.make!(:username => nil)
Query(User)

# Q 43 : # User.make!(:username => nil)
Query(User)

# Q 44 : # User.make!
Query(User)

# Q 45 : # User.make!(:username => nil)
Query(User)

# Q 46 : # User.make!
Query(User)

# Q 47 : # User.make!
Query(User)

# Q 48 : # @user = User.make!
Query(User)

# Q 49 : # @user = User.make!
Query(User)

# Q 50 : # User.make!
Query(User)

# Q 51 : # Story.make!(:title => "hello", :url => "http://example.com/")
Query(Story)

# Q 52 : # Story.make!
Query(Story)

# Q 53 : # Story.make!(:title => "hello", :url => "http://example.com/")
Query(Story)

# Q 54 : # Story.make!
Query(Story)

# Q 55 : # Story.make!(:title => "hello", :url => "http://example.com/")
Query(Story)

# Q 56 : # Story.make!
Query(Story)

# Q 57 : # Story.make!
Query(Story)

# Q 58 : # Comment.make!(:comment => "hello")
Query(Comment)

# Q 59 : # Comment.make!
Query(Comment)

# Q 60 : # Comment.make!(:comment => "hello")
Query(Comment)

# Q 61 : # Comment.make!
Query(Comment)

# Q 62 : # Comment.make!(:comment => "hello")
Query(Comment)

# Q 63 : # Comment.make!
Query(Comment)

# Q 64 : # Comment.make!
Query(Comment)

# Q 65 : # Story.make!
Query(Story)

# Q 66 : # s = Story.make!
Query(Story)

# Q 67 : # s = Story.make!
Query(Story)

# Q 68 : # Story.make!
Query(Story)

# Q 69 : # Message.make!
Query(Message)

# Q 70 : # m = Message.make!
Query(Message)

# Q 71 : # m = Message.make!
Query(Message)

# Q 72 : # Message.make!
Query(Message)

# Q 73 : # if comment.errors.any?
#   
#   
#   errors_for comment
# end
Query(Comment)

# Q 74 : # comment.errors.any?
Query(Comment)

# Q 75 : # comment.errors
Query(Comment)

# Q 76 : # comment.persisted?
Query(Comment)

# Q 77 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 78 : # @comment.url
Query(Comment)

# Q 79 : # @comment.url
Query(Comment)

# Q 80 : # story.score
Query(Story)

# Q 81 : # Moderation.count
Query(Moderation)

# Q 82 : # Moderation.count
Query(Moderation)

# Q 83 : # Search.new
Query(Search)

# Q 84 : # Search.new
Query(Search)

# Q 85 : # Search.new
Query(Search)

# Q 86 : # Tag.all_with_story_counts_for(nil)
Query(Tag)

# Q 87 : # Tag.all_with_story_counts_for(nil)
Query(Tag)

# Q 88 : # Tag.all_with_story_counts_for
Query(Tag)

# Q 89 : # Tag.all_with_story_counts_for
Query(Tag)

# Q 90 : # User.make!(:username => "")
Query(User)

# Q 91 : # User.make!
Query(User)

# Q 92 : # User.make!(:username => "")
Query(User)

# Q 93 : # User.make!
Query(User)

# Q 94 : # User.make!(:username => "")
Query(User)

# Q 95 : # User.make!(:username => "")
Query(User)

# Q 96 : # User.make!
Query(User)

# Q 97 : # User.make!(:username => "")
Query(User)

# Q 98 : # User.make!
Query(User)

# Q 99 : # Story.make!(:user => @user)
Query(Story)

# Q 100 : # Story.make!
Query(Story)

# Q 101 : # Story.make!(:user => @user)
Query(Story)

# Q 102 : # Story.make!
Query(Story)

# Q 103 : # Story.make!(:user => @user)
Query(Story)

# Q 104 : # Story.make!
Query(Story)

# Q 105 : # Story.make!
Query(Story)

# Q 106 : # comment.current_vote
Query(Comment)

# Q 107 : # comment.current_vote
Query(Comment)

# Q 108 : # @hat_requests.count
Query(HatRequest)

# Q 109 : # @tags.map { |t|
#   
#   t.stories_count
# }.max
Query(Tag)

# Q 110 : # @tags.map
Query(Tag)

# Q 111 : # @invitation_request.name
Query(InvitationRequest)
.select('name')
# Q 112 : # story.score
Query(Story)

# Q 113 : # @story.short_id
Query(Story)
.select('short_id')
# Q 114 : # @story.short_id
Query(Story)
.select('short_id')
# Q 115 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 116 : # self.where(:key => key)
Query(Keystore)
.where("key = ?")
# Q 117 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 118 : # @user.stories_submitted_count
Query(User)

# Q 119 : # @user.stories_submitted_count
Query(User)

# Q 120 : # InvitationRequest.new
Query(InvitationRequest)

# Q 121 : # InvitationRequest.new
Query(InvitationRequest)

# Q 122 : # InvitationRequest.new
Query(InvitationRequest)

# Q 123 : # @user.dup
Query(User)

# Q 124 : # @user.dup
Query(User)

# Q 125 : # @user.dup
Query(User)

# Q 126 : # User.make!(:username => "*")
Query(User)

# Q 127 : # User.make!
Query(User)

# Q 128 : # User.make!(:username => "*")
Query(User)

# Q 129 : # User.make!
Query(User)

# Q 130 : # User.make!(:username => "*")
Query(User)

# Q 131 : # User.make!(:username => "*")
Query(User)

# Q 132 : # User.make!
Query(User)

# Q 133 : # User.make!(:username => "*")
Query(User)

# Q 134 : # User.make!
Query(User)

# Q 135 : # @tags.each
Query(Tag)

# Q 136 : # @invitation_request.email
Query(InvitationRequest)
.select('email')
# Q 137 : # @users.each
Query(User)

# Q 138 : # @invitation.code
Query(Invitation)
.select('code')
# Q 139 : # @story.markeddown_description.present?
Query(Story)
.select('markeddown_description')
# Q 140 : # @story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 141 : # story.is_hidden_by_cur_user
Query(Story)

# Q 142 : # @user.password_reset_token
Query(User)
.select('password_reset_token')
# Q 143 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize.save!
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 144 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 145 : # HiddenStory.where(:user_id => user_id, :story_id => story_id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 146 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize.save!
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 147 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 148 : # Tag.active.all_with_story_counts_for(@user)
Query(Tag)

# Q 149 : # Tag.active.all_with_story_counts_for(@user)
Query(Tag)

# Q 150 : # Tag.active.all_with_story_counts_for
Query(Tag)

# Q 151 : # Tag.active
Query(Tag)

# Q 152 : # Tag.active.all_with_story_counts_for
Query(Tag)

# Q 153 : # Tag.active
Query(Tag)

# Q 154 : # User.make!
Query(User)

# Q 155 : # @commentor = User.make!
Query(User)

# Q 156 : # @commentor = User.make!
Query(User)

# Q 157 : # User.make!
Query(User)

# Q 158 : # comment.highlighted
Query(Comment)

# Q 159 : # tag.stories_count.to_f
Query(Tag)

# Q 160 : # tag.stories_count
Query(Tag)

# Q 161 : # max_size.to_f / tag.stories_count.to_f
Query(Tag)

# Q 162 : # tag.stories_count.to_f
Query(Tag)

# Q 163 : # tag.stories_count
Query(Tag)

# Q 164 : # @invitation_request.memo
Query(InvitationRequest)
.select('memo')
# Q 165 : # @user.invited_by_user.try
Query(User)
.where("id = ?")
# Q 166 : # @user.invited_by_user
Query(User)
.where("id = ?")
# Q 167 : # @invitation.code
Query(Invitation)
.select('code')
# Q 168 : # @invitation.code
Query(Invitation)
.select('code')
# Q 169 : # @search.q
Query(Search)

# Q 170 : # @search.q
Query(Search)

# Q 171 : # story.is_expired?
Query(Story)

# Q 172 : # where(:inactive => false)
Query(Tag)
.where("inactive = ?")
# Q 173 : # HatRequest.new
Query(HatRequest)

# Q 174 : # HatRequest.new
Query(HatRequest)

# Q 175 : # HatRequest.new
Query(HatRequest)

# Q 176 : # Message.new
Query(Message)

# Q 177 : # Message.new
Query(Message)

# Q 178 : # Message.new
Query(Message)

# Q 179 : # User.make!(:username => "test")
Query(User)

# Q 180 : # User.make!
Query(User)

# Q 181 : # User.make!(:username => "test")
Query(User)

# Q 182 : # User.make!(:username => "test")
Query(User)

# Q 183 : # User.make!
Query(User)

# Q 184 : # Comment.make!(:story => @story, :user => @commentor)
Query(Comment)

# Q 185 : # Comment.make!
Query(Comment)

# Q 186 : # Comment.make!(:story => @story, :user => @commentor)
Query(Comment)

# Q 187 : # Comment.make!
Query(Comment)

# Q 188 : # Comment.make!(:story => @story, :user => @commentor)
Query(Comment)

# Q 189 : # Comment.make!
Query(Comment)

# Q 190 : # Comment.make!
Query(Comment)

# Q 191 : # comment.story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 192 : # comment.story
Query(Story)
.where("id = ?")
# Q 193 : # comment.story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 194 : # comment.story
Query(Story)
.where("id = ?")
# Q 195 : # comment.score
Query(Comment)

# Q 196 : # @hat_requests.each_with_index
Query(HatRequest)

# Q 197 : # tag.tag
Query(Tag)
.select('tag')
# Q 198 : # tag.css_class
Query(Tag)

# Q 199 : # tag.tag
Query(Tag)
.select('tag')
# Q 200 : # tag.css_class
Query(Tag)

# Q 201 : # user.username
Query(User)
.select('username')
# Q 202 : # user.username
Query(User)
.select('username')
# Q 203 : # @story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 204 : # InvitationRequest.where(:is_verified => true).count
Query(InvitationRequest)
.where("is_verified = ?")
# Q 205 : # InvitationRequest.where(:is_verified => true)
Query(InvitationRequest)
.where("is_verified = ?")
# Q 206 : # InvitationRequest.where(:is_verified => true).count
Query(InvitationRequest)
.where("is_verified = ?")
# Q 207 : # User.make!(:username => "test")
Query(User)

# Q 208 : # User.make!
Query(User)

# Q 209 : # User.make!(:username => "test")
Query(User)

# Q 210 : # User.make!
Query(User)

# Q 211 : # User.make!(:username => "test")
Query(User)

# Q 212 : # User.make!(:username => "test")
Query(User)

# Q 213 : # User.make!
Query(User)

# Q 214 : # User.make!(:username => "test")
Query(User)

# Q 215 : # User.make!
Query(User)

# Q 216 : # @stories.each
Query(Story)

# Q 217 : # comment.score
Query(Comment)

# Q 218 : # @comments.each
Query(Comment)

# Q 219 : # user.is_active?
Query(User)

# Q 220 : # user.is_active?
Query(User)

# Q 221 : # self.where(:key => key).first.try(:value)
Query(Keystore)
.where("key = ?")
.return_limit('1')
.select('value')
# Q 222 : # self.where(:key => key).first.try
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 223 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 224 : # self.where(:key => key)
Query(Keystore)
.where("key = ?")
# Q 225 : # self.where(:key => key).first.try
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 226 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 227 : # Moderation.joins(:story).where("stories.user_id = ? AND moderations.created_at > ?", @user.id, 5.days.ago).count
Query(Moderation)
.joins('story')
.where("user_id = ?")
# Q 228 : # Moderation.joins(:story).where("stories.user_id = ? AND moderations.created_at > ?", @user.id, 5.days.ago)
Query(Moderation)
.joins('story')
.where("user_id = ?")
# Q 229 : # Moderation.joins(:story).where
Query(Moderation)
.joins('story')
# Q 230 : # Moderation.joins(:story)
Query(Moderation)
.joins('story')
# Q 231 : # Moderation.joins
Query(Moderation)

# Q 232 : # Moderation.joins(:story).where("stories.user_id = ? AND moderations.created_at > ?", @user.id, 5.days.ago).count
Query(Moderation)
.joins('story')
.where("user_id = ?")
# Q 233 : # Moderation.joins(:story).where
Query(Moderation)
.joins('story')
# Q 234 : # Moderation.joins
Query(Moderation)

# Q 235 : # @user.tag_filter_tags.to_a
Query(Tag)
.where("user_id = ?")
# Q 236 : # @user.tag_filter_tags.to_a
Query(Tag)
.where("user_id = ?")
# Q 237 : # @user.tag_filter_tags
Query(Tag)
.where("user_id = ?")
# Q 238 : # @user.tag_filter_tags.to_a
Query(Tag)
.where("user_id = ?")
# Q 239 : # @user.tag_filter_tags
Query(Tag)
.where("user_id = ?")
# Q 240 : # @user.try(:authenticate, params[:user][:password].to_s)
Query(User)
.select('authenticate')
# Q 241 : # @user.try
Query(User)

# Q 242 : # @user.try
Query(User)

# Q 243 : # User.make!(:mailing_list_mode => 1)
Query(User)

# Q 244 : # User.make!
Query(User)

# Q 245 : # User.make!(:mailing_list_mode => 1)
Query(User)

# Q 246 : # User.make!
Query(User)

# Q 247 : # User.make!(:mailing_list_mode => 1)
Query(User)

# Q 248 : # User.make!
Query(User)

# Q 249 : # User.make!
Query(User)

# Q 250 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 251 : # Story.make!
Query(Story)

# Q 252 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 253 : # Story.make!
Query(Story)

# Q 254 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 255 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 256 : # Story.make!
Query(Story)

# Q 257 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 258 : # Story.make!
Query(Story)

# Q 259 : # User.make!
Query(User)

# Q 260 : # u = User.make!
Query(User)

# Q 261 : # u = User.make!
Query(User)

# Q 262 : # User.make!
Query(User)

# Q 263 : # if comment.parent_comment
#   
#   
#   hidden_field_tag "parent_comment_short_id", comment.parent_comment.short_id
# end
Query(Comment)

# Q 264 : # comment.parent_comment
Query(Comment)
.where("id = ?")
# Q 265 : # comment.is_gone?
Query(Comment)

# Q 266 : # @message.subject
Query(Message)
.select('subject')
# Q 267 : # if @user.is_moderator?
#   
#   
#   f.label :merge_story_short_id, "Merge Into:", :class => "required"
#   f.text_field :merge_story_short_id, :autocomplete => "off", :placeholder => "Short id of story into which this story " << "be merged"
#   f.label :unavailable_at, "Unavailable:", :class => "required"
#   f.check_box :is_unavailable
#   f.label :unavailable_at, "Source URL is unavailable, " << "enable display of cached text", :class => "normal"
#   if @story.user_id != @user.id
#     
#     
#     f.label :moderation_reason, "Mod Reason:", :class => "required"
#     f.text_field :moderation_reason, :autocomplete => "off"
#   end
# end
Query(User)

# Q 268 : # @user.is_moderator?
Query(User)

# Q 269 : # self.tag
Query(Tag)
.select('tag')
# Q 270 : # self.tag
Query(Tag)
.select('tag')
# Q 271 : # Message.new
Query(Message)

# Q 272 : # Message.new
Query(Message)

# Q 273 : # Message.new
Query(Message)

# Q 274 : # Moderation.new
Query(Moderation)

# Q 275 : # Moderation.new
Query(Moderation)

# Q 276 : # Moderation.new
Query(Moderation)

# Q 277 : # self.transaction
Query(HatRequest)

# Q 278 : # self.transaction
Query(HatRequest)

# Q 279 : # @user.id
Query(User)

# Q 280 : # @user.id
Query(User)

# Q 281 : # @user.undeleted_received_messages
Query(User)

# Q 282 : # @user.undeleted_received_messages
Query(User)

# Q 283 : # @user.undeleted_received_messages
Query(User)

# Q 284 : # @user.delete!
Query(User)

# Q 285 : # @user.delete!
Query(User)

# Q 286 : # User.where(:session_token => session[:u].to_s).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 287 : # User.where(:session_token => session[:u].to_s).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 288 : # User.where(:session_token => session[:u].to_s)
Query(User)
.where("session_token = ?")
# Q 289 : # User.where(:session_token => session[:u].to_s).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 290 : # story.title
Query(Story)
.select('title')
# Q 291 : # story.title
Query(Story)
.select('title')
# Q 292 : # comment.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 293 : # comment.story
Query(Story)
.where("id = ?")
# Q 294 : # comment.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 295 : # comment.story
Query(Story)
.where("id = ?")
# Q 296 : # user.is_new?
Query(User)

# Q 297 : # user.is_new?
Query(User)

# Q 298 : # self.moderator_user_id
Query(Moderation)
.select('moderator_user_id')
# Q 299 : # self.moderator_user_id
Query(Moderation)
.select('moderator_user_id')
# Q 300 : # self.moderator_user_id
Query(Moderation)
.select('moderator_user_id')
# Q 301 : # self.user_id
Query(Hat)
.select('user_id')
# Q 302 : # self.user_id
Query(Hat)
.select('user_id')
# Q 303 : # self.user_id
Query(Hat)
.select('user_id')
# Q 304 : # Hat.new
Query(Hat)

# Q 305 : # Hat.new
Query(Hat)

# Q 306 : # h = Hat.new
Query(Hat)

# Q 307 : # Hat.new
Query(Hat)

# Q 308 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 309 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 310 : # Story.where(:short_id => params[:story_id])
Query(Story)
.where("short_id = ?")
# Q 311 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 312 : # user.is_active?
Query(User)

# Q 313 : # user.is_active?
Query(User)

# Q 314 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 315 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 316 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 317 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 318 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 319 : # story.url_or_comments_url
Query(Story)

# Q 320 : # story.url_or_comments_url
Query(Story)

# Q 321 : # comment.parent_comment.short_id
Query(Comment)
.where("id = ?")
.select('short_id')
# Q 322 : # comment.parent_comment
Query(Comment)
.where("id = ?")
# Q 323 : # comment.parent_comment.short_id
Query(Comment)
.where("id = ?")
.select('short_id')
# Q 324 : # comment.parent_comment
Query(Comment)
.where("id = ?")
# Q 325 : # comment.url
Query(Comment)

# Q 326 : # comment.url
Query(Comment)

# Q 327 : # @moderations.each
Query(Moderation)

# Q 328 : # @invitation_request.code
Query(InvitationRequest)
.select('code')
# Q 329 : # @story.is_unavailable
Query(Story)

# Q 330 : # @story.story_cache.present?
Query(Story)
.select('story_cache')
# Q 331 : # @story.story_cache
Query(Story)
.select('story_cache')
# Q 332 : # user.id
Query(User)

# Q 333 : # user.id
Query(User)

# Q 334 : # user.id
Query(User)

# Q 335 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 336 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 337 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 338 : # Story.new(story_params)
Query(Story)

# Q 339 : # Story.new(story_params)
Query(Story)

# Q 340 : # Story.new
Query(Story)

# Q 341 : # Story.new
Query(Story)

# Q 342 : # Moderation.order("id desc").limit(50).offset((
# @page - 1) * 50)
Query(Moderation)
.order('id')
.order('id')
.return_limit('')
# Q 343 : # Moderation.order("id desc").limit(50).offset((
# @page - 1) * 50)
Query(Moderation)
.order('id')
.order('id')
.return_limit('')
# Q 344 : # Moderation.order("id desc").limit(50).offset
Query(Moderation)
.order('id')
.order('id')
.return_limit('')
# Q 345 : # Moderation.order("id desc").limit(50)
Query(Moderation)
.order('id')
.order('id')
.return_limit('')
# Q 346 : # Moderation.order("id desc").limit
Query(Moderation)
.order('id')
.order('id')
.return_limit('')
# Q 347 : # Moderation.order("id desc")
Query(Moderation)
.order('id')
.order('id')
# Q 348 : # Moderation.order
Query(Moderation)

# Q 349 : # Moderation.order("id desc").limit(50).offset
Query(Moderation)
.order('id')
.order('id')
.return_limit('')
# Q 350 : # Moderation.order("id desc").limit
Query(Moderation)
.order('id')
.order('id')
.return_limit('')
# Q 351 : # Moderation.order
Query(Moderation)

# Q 352 : # story.is_gone?
Query(Story)

# Q 353 : # story.is_gone?
Query(Story)

# Q 354 : # User.make!(:email => "user@example.com")
Query(User)

# Q 355 : # User.make!
Query(User)

# Q 356 : # User.make!(:email => "user@example.com")
Query(User)

# Q 357 : # User.make!(:email => "user@example.com")
Query(User)

# Q 358 : # User.make!
Query(User)

# Q 359 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 360 : # Story.make!
Query(Story)

# Q 361 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 362 : # Story.make!
Query(Story)

# Q 363 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 364 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 365 : # Story.make!
Query(Story)

# Q 366 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 367 : # Story.make!
Query(Story)

# Q 368 : # story.short_id_url
Query(Story)

# Q 369 : # story.short_id_url
Query(Story)

# Q 370 : # comment.id
Query(Comment)

# Q 371 : # comment.id
Query(Comment)

# Q 372 : # comment.id
Query(Comment)

# Q 373 : # comment.id
Query(Comment)

# Q 374 : # comment.id
Query(Comment)

# Q 375 : # comment.short_id_url
Query(Comment)

# Q 376 : # comment.short_id_url
Query(Comment)

# Q 377 : # self.hat
Query(Hat)
.select('hat')
# Q 378 : # self.hat
Query(Hat)
.select('hat')
# Q 379 : # user.id
Query(User)

# Q 380 : # user.id
Query(User)

# Q 381 : # user.id
Query(User)

# Q 382 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 383 : # Keystore.connection
Query(Keystore)

# Q 384 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 385 : # Keystore.connection
Query(Keystore)

# Q 386 : # @user.id
Query(User)

# Q 387 : # @user.id
Query(User)

# Q 388 : # @user.id
Query(User)

# Q 389 : # InvitationRequest.where(:is_verified => true)
Query(InvitationRequest)
.where("is_verified = ?")
# Q 390 : # InvitationRequest.where(:is_verified => true)
Query(InvitationRequest)
.where("is_verified = ?")
# Q 391 : # @user.id
Query(User)

# Q 392 : # @user.username
Query(User)
.select('username')
# Q 393 : # @user.id
Query(User)

# Q 394 : # @user.username
Query(User)
.select('username')
# Q 395 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 396 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 397 : # story.user
Query(User)
.where("id = ?")
# Q 398 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 399 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 400 : # comment.user
Query(User)
.where("id = ?")
# Q 401 : # @message.author
Query(User)
.where("id = ?")
# Q 402 : # user.username
Query(User)
.select('username')
# Q 403 : # user.username
Query(User)
.select('username')
# Q 404 : # @story.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 405 : # TagFilter.group(:tag_id).count
Query(TagFilter)
.group('tag_id')
# Q 406 : # TagFilter.group(:tag_id).count
Query(TagFilter)
.group('tag_id')
# Q 407 : # TagFilter.group(:tag_id)
Query(TagFilter)
.group('tag_id')
# Q 408 : # TagFilter.group
Query(TagFilter)
.group('')
# Q 409 : # TagFilter.group(:tag_id).count
Query(TagFilter)
.group('tag_id')
# Q 410 : # TagFilter.group
Query(TagFilter)
.group('')
# Q 411 : # self.assign_short_id_and_upvote
Query(Comment)

# Q 412 : # self.assign_short_id_and_upvote
Query(Comment)

# Q 413 : # where(:has_been_read => false, :deleted_by_recipient => false)
Query(Message)
.where("has_been_read = ?")
.where("deleted_by_recipient = ?")
# Q 414 : # self.hat
Query(HatRequest)
.select('hat')
# Q 415 : # self.hat
Query(HatRequest)
.select('hat')
# Q 416 : # self.hat
Query(HatRequest)
.select('hat')
# Q 417 : # Keystore.connection.execute
Query(Keystore)

# Q 418 : # Keystore.connection
Query(Keystore)

# Q 419 : # Keystore.connection.execute
Query(Keystore)

# Q 420 : # Keystore.connection
Query(Keystore)

# Q 421 : # story.created_at.rfc2822
Query(Story)
.select('created_at')
# Q 422 : # story.created_at.rfc2822
Query(Story)
.select('created_at')
# Q 423 : # story.created_at
Query(Story)
.select('created_at')
# Q 424 : # comment.created_at.rfc2822
Query(Comment)
.select('created_at')
# Q 425 : # comment.created_at.rfc2822
Query(Comment)
.select('created_at')
# Q 426 : # comment.created_at
Query(Comment)
.select('created_at')
# Q 427 : # @comments.any?
Query(Comment)

# Q 428 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 429 : # @message.author
Query(User)
.where("id = ?")
# Q 430 : # if user.is_admin?
#   
#   
# else
#   
#   
#   user.karma
#   if user.is_moderator?
#     
#     
#   end
# end
Query(User)

# Q 431 : # user.is_admin?
Query(User)

# Q 432 : # @search.what
Query(Search)

# Q 433 : # story.score
Query(Story)

# Q 434 : # @story.short_id
Query(Story)
.select('short_id')
# Q 435 : # self.assign_initial_confidence
Query(Comment)

# Q 436 : # self.assign_initial_confidence
Query(Comment)

# Q 437 : # self.link
Query(HatRequest)
.select('link')
# Q 438 : # self.link
Query(HatRequest)
.select('link')
# Q 439 : # self.link
Query(HatRequest)
.select('link')
# Q 440 : # Keystore.table_name
Query(Keystore)

# Q 441 : # Keystore.table_name
Query(Keystore)

# Q 442 : # Hat.all.includes(:user).each
Query(Hat)
.includes('user')
# Q 443 : # Hat.all.includes(:user)
Query(Hat)
.includes('user')
# Q 444 : # Hat.all.includes
Query(Hat)

# Q 445 : # Hat.all
Query(Hat)

# Q 446 : # Hat.all.includes(:user).each
Query(Hat)
.includes('user')
# Q 447 : # Hat.all.includes
Query(Hat)

# Q 448 : # Hat.all
Query(Hat)

# Q 449 : # @story.valid?
Query(Story)

# Q 450 : # @story.already_posted_story
Query(Story)

# Q 451 : # @story.seen_previous
Query(Story)

# Q 452 : # @story.valid?
Query(Story)

# Q 453 : # @story.already_posted_story
Query(Story)

# Q 454 : # @story.seen_previous
Query(Story)

# Q 455 : # User.make!(:email => "user@example.com")
Query(User)

# Q 456 : # User.make!
Query(User)

# Q 457 : # User.make!(:email => "user@example.com")
Query(User)

# Q 458 : # User.make!
Query(User)

# Q 459 : # User.make!(:email => "user@example.com")
Query(User)

# Q 460 : # User.make!(:email => "user@example.com")
Query(User)

# Q 461 : # User.make!
Query(User)

# Q 462 : # User.make!(:email => "user@example.com")
Query(User)

# Q 463 : # User.make!
Query(User)

# Q 464 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 465 : # Story.make!
Query(Story)

# Q 466 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 467 : # Story.make!
Query(Story)

# Q 468 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 469 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 470 : # Story.make!
Query(Story)

# Q 471 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 472 : # Story.make!
Query(Story)

# Q 473 : # story.comments_url
Query(Story)

# Q 474 : # story.comments_url
Query(Story)

# Q 475 : # comment.comment
Query(Comment)
.select('comment')
# Q 476 : # comment.comment
Query(Comment)
.select('comment')
# Q 477 : # comment.url
Query(Comment)

# Q 478 : # comment.url
Query(Comment)

# Q 479 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 480 : # @message.author
Query(User)
.where("id = ?")
# Q 481 : # User.username_regex
Query(User)

# Q 482 : # User.username_regex
Query(User)

# Q 483 : # CandidateId.new(klass)
Query(CandidateId)

# Q 484 : # CandidateId.new
Query(CandidateId)

# Q 485 : # CandidateId.new
Query(CandidateId)

# Q 486 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 487 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 488 : # Tag.active.order(:tag)
Query(Tag)
.order('tag')
# Q 489 : # Tag.active.order
Query(Tag)

# Q 490 : # Tag.active
Query(Tag)

# Q 491 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 492 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 493 : # Tag.active.order
Query(Tag)

# Q 494 : # Tag.active
Query(Tag)

# Q 495 : # self.assign_thread_id
Query(Comment)

# Q 496 : # self.assign_thread_id
Query(Comment)

# Q 497 : # self.story
Query(Story)
.where("id = ?")
# Q 498 : # self.story
Query(Story)
.where("id = ?")
# Q 499 : # self.destroy
Query(Hat)

# Q 500 : # self.destroy
Query(Hat)

# Q 501 : # @story.save
Query(Story)

# Q 502 : # @story.save
Query(Story)

# Q 503 : # User.order("karma DESC, id ASC").to_a
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 504 : # User.order("karma DESC, id ASC").to_a
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 505 : # User.order("karma DESC, id ASC")
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 506 : # User.order
Query(User)

# Q 507 : # User.order("karma DESC, id ASC").to_a
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 508 : # User.order
Query(User)

# Q 509 : # story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 510 : # story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 511 : # story.comments
Query(Comment)
.where("story_id = ?")
# Q 512 : # story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 513 : # story.comments
Query(Comment)
.where("story_id = ?")
# Q 514 : # User.make!(:username => "blahblah")
Query(User)

# Q 515 : # User.make!
Query(User)

# Q 516 : # User.make!(:username => "blahblah")
Query(User)

# Q 517 : # User.make!(:username => "blahblah")
Query(User)

# Q 518 : # User.make!
Query(User)

# Q 519 : # comment.score
Query(Comment)

# Q 520 : # comment.markeddown_comment
Query(Comment)
.select('markeddown_comment')
# Q 521 : # comment.markeddown_comment
Query(Comment)
.select('markeddown_comment')
# Q 522 : # @message.author.is_admin?
Query(User)
.where("id = ?")
# Q 523 : # @message.author
Query(User)
.where("id = ?")
# Q 524 : # @user.is_moderator?
Query(User)

# Q 525 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 526 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 527 : # self.story
Query(Story)
.where("id = ?")
# Q 528 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 529 : # self.story
Query(Story)
.where("id = ?")
# Q 530 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 531 : # Keystore.connection
Query(Keystore)

# Q 532 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 533 : # Keystore.connection
Query(Keystore)

# Q 534 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 535 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 536 : # InvitationRequest.where(:code => params[:code].to_s)
Query(InvitationRequest)
.where("code = ?")
# Q 537 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 538 : # @users.length
Query(User)

# Q 539 : # @users.length
Query(User)

# Q 540 : # @users.length
Query(User)

# Q 541 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 542 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 543 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 544 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 545 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 546 : # story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 547 : # story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 548 : # @user.can_downvote?
Query(User)

# Q 549 : # user.karma
Query(User)
.select('karma')
# Q 550 : # user.karma
Query(User)
.select('karma')
# Q 551 : # InvitationRequest.exists?(:code => self.code)
Query(InvitationRequest)
.return_limit('1')
# Q 552 : # InvitationRequest.exists?
Query(InvitationRequest)
.return_limit('1')
# Q 553 : # self.code
Query(InvitationRequest)
.select('code')
# Q 554 : # InvitationRequest.exists?(:code => self.code)
Query(InvitationRequest)
.return_limit('1')
# Q 555 : # InvitationRequest.exists?
Query(InvitationRequest)
.return_limit('1')
# Q 556 : # self.code
Query(InvitationRequest)
.select('code')
# Q 557 : # InvitationRequest.exists?
Query(InvitationRequest)
.return_limit('1')
# Q 558 : # self.code
Query(InvitationRequest)
.select('code')
# Q 559 : # Invitation.exists?(:code => self.code)
Query(Invitation)
.return_limit('1')
# Q 560 : # Invitation.exists?
Query(Invitation)
.return_limit('1')
# Q 561 : # self.code
Query(Invitation)
.select('code')
# Q 562 : # Invitation.exists?(:code => self.code)
Query(Invitation)
.return_limit('1')
# Q 563 : # Invitation.exists?
Query(Invitation)
.return_limit('1')
# Q 564 : # self.code
Query(Invitation)
.select('code')
# Q 565 : # Invitation.exists?
Query(Invitation)
.return_limit('1')
# Q 566 : # self.code
Query(Invitation)
.select('code')
# Q 567 : # Message.new
Query(Message)

# Q 568 : # Message.new
Query(Message)

# Q 569 : # m = Message.new
Query(Message)

# Q 570 : # Message.new
Query(Message)

# Q 571 : # Keystore.connection.execute
Query(Keystore)

# Q 572 : # Keystore.connection
Query(Keystore)

# Q 573 : # Keystore.table_name
Query(Keystore)

# Q 574 : # Keystore.connection.execute
Query(Keystore)

# Q 575 : # Keystore.connection
Query(Keystore)

# Q 576 : # Keystore.table_name
Query(Keystore)

# Q 577 : # Tag.active.where(:tag => tags_param).to_a
Query(Tag)
.where("tag = ?")
# Q 578 : # Tag.active.where(:tag => tags_param)
Query(Tag)
.where("tag = ?")
# Q 579 : # Tag.active.where
Query(Tag)

# Q 580 : # Tag.active
Query(Tag)

# Q 581 : # Tag.active.where(:tag => tags_param).to_a
Query(Tag)
.where("tag = ?")
# Q 582 : # Tag.active.where
Query(Tag)

# Q 583 : # Tag.active
Query(Tag)

# Q 584 : # User.where(:email => params[:email]).first
Query(User)
.where("email = ?")
.return_limit('1')
# Q 585 : # User.where(:email => params[:email]).first
Query(User)
.where("email = ?")
.return_limit('1')
# Q 586 : # User.where(:email => params[:email])
Query(User)
.where("email = ?")
# Q 587 : # User.where(:email => params[:email]).first
Query(User)
.where("email = ?")
.return_limit('1')
# Q 588 : # User.make!(:email => "user@")
Query(User)

# Q 589 : # User.make!
Query(User)

# Q 590 : # User.make!(:email => "user@")
Query(User)

# Q 591 : # User.make!
Query(User)

# Q 592 : # User.make!(:email => "user@")
Query(User)

# Q 593 : # User.make!(:email => "user@")
Query(User)

# Q 594 : # User.make!
Query(User)

# Q 595 : # User.make!(:email => "user@")
Query(User)

# Q 596 : # User.make!
Query(User)

# Q 597 : # if story.url.present?
#   
#   
#   raw coder.encode("<p>" + link_to("Comments", story.comments_url) + "</p>", :decimal)
# end
Query(Story)

# Q 598 : # story.url.present?
Query(Story)
.select('url')
# Q 599 : # story.url
Query(Story)
.select('url')
# Q 600 : # @message.author.is_moderator?
Query(User)
.where("id = ?")
# Q 601 : # @message.author
Query(User)
.where("id = ?")
# Q 602 : # if user.is_moderator?
#   
#   
# end
Query(User)

# Q 603 : # user.is_moderator?
Query(User)

# Q 604 : # story.can_be_seen_by_user?
Query(Story)

# Q 605 : # self.is_from_suggestions?
Query(Moderation)

# Q 606 : # self.is_from_suggestions?
Query(Moderation)

# Q 607 : # user.id
Query(User)

# Q 608 : # user.id
Query(User)

# Q 609 : # user.id
Query(User)

# Q 610 : # where(:merged_story_id => nil)
Query(Story)
.where("merged_story_id = ?")
# Q 611 : # Story.arel_table
Query(Story)

# Q 612 : # Story.arel_table
Query(Story)

# Q 613 : # @search.valid?
Query(Search)

# Q 614 : # @search.valid?
Query(Search)

# Q 615 : # user.username
Query(User)
.select('username')
# Q 616 : # @search.what
Query(Search)

# Q 617 : # story.url_or_comments_path
Query(Story)

# Q 618 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 619 : # self.story
Query(Story)
.where("id = ?")
# Q 620 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 621 : # self.story
Query(Story)
.where("id = ?")
# Q 622 : # self.link.present?
Query(Hat)
.select('link')
# Q 623 : # self.link
Query(Hat)
.select('link')
# Q 624 : # self.link.match(/^https?:\/\//)
Query(Hat)
.select('link')
# Q 625 : # self.link.match
Query(Hat)
.select('link')
# Q 626 : # self.link
Query(Hat)
.select('link')
# Q 627 : # self.link.present?
Query(Hat)
.select('link')
# Q 628 : # self.link
Query(Hat)
.select('link')
# Q 629 : # self.link.match
Query(Hat)
.select('link')
# Q 630 : # self.link
Query(Hat)
.select('link')
# Q 631 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 632 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 633 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 634 : # User.where(:username => params[:email]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 635 : # User.where(:username => params[:email]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 636 : # User.where(:username => params[:email])
Query(User)
.where("username = ?")
# Q 637 : # User.where(:username => params[:email]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 638 : # @story.comments_path
Query(Story)

# Q 639 : # @story.comments_path
Query(Story)

# Q 640 : # @search.search_for_user!(@user)
Query(Search)

# Q 641 : # @search.search_for_user!
Query(Search)

# Q 642 : # @search.search_for_user!
Query(Search)

# Q 643 : # @user.hats.where(:id => params[:hat_id])
Query(Hat)
.where("user_id = ?")
.where("id = ?")
# Q 644 : # @user.hats.where
Query(Hat)
.where("user_id = ?")
# Q 645 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 646 : # @user.hats.where
Query(Hat)
.where("user_id = ?")
# Q 647 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 648 : # Story.make!(:title => "")
Query(Story)

# Q 649 : # Story.make!
Query(Story)

# Q 650 : # Story.make!(:title => "")
Query(Story)

# Q 651 : # Story.make!
Query(Story)

# Q 652 : # Story.make!(:title => "")
Query(Story)

# Q 653 : # Story.make!(:title => "")
Query(Story)

# Q 654 : # Story.make!
Query(Story)

# Q 655 : # Story.make!(:title => "")
Query(Story)

# Q 656 : # Story.make!
Query(Story)

# Q 657 : # story.comments_url
Query(Story)

# Q 658 : # story.comments_url
Query(Story)

# Q 659 : # user.is_active?
Query(User)

# Q 660 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 661 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 662 : # @invitation.user
Query(User)
.where("id = ?")
# Q 663 : # story.title
Query(Story)
.select('title')
# Q 664 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 665 : # self.story
Query(Story)
.where("id = ?")
# Q 666 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 667 : # self.story
Query(Story)
.where("id = ?")
# Q 668 : # self.hat
Query(HatRequest)
.select('hat')
# Q 669 : # self.hat
Query(HatRequest)
.select('hat')
# Q 670 : # self.hat
Query(HatRequest)
.select('hat')
# Q 671 : # self.hat
Query(HatRequest)
.select('hat')
# Q 672 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 673 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 674 : # Invitation.where(:code => params[:invitation_code].to_s)
Query(Invitation)
.where("code = ?")
# Q 675 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 676 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC").to_a
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 677 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC").to_a
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 678 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC")
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 679 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order
Query(User)
.where(" = ?")
# Q 680 : # User.where("is_admin = ? OR is_moderator = ?", true, true)
Query(User)
.where(" = ?")
# Q 681 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC").to_a
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 682 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order
Query(User)
.where(" = ?")
# Q 683 : # Story.make!(:title => "hi")
Query(Story)

# Q 684 : # Story.make!
Query(Story)

# Q 685 : # Story.make!(:title => "hi")
Query(Story)

# Q 686 : # Story.make!
Query(Story)

# Q 687 : # Story.make!(:title => "hi")
Query(Story)

# Q 688 : # Story.make!(:title => "hi")
Query(Story)

# Q 689 : # Story.make!
Query(Story)

# Q 690 : # Story.make!(:title => "hi")
Query(Story)

# Q 691 : # Story.make!
Query(Story)

# Q 692 : # Story.make!
Query(Story)

# Q 693 : # s = Story.make!
Query(Story)

# Q 694 : # s = Story.make!
Query(Story)

# Q 695 : # Story.make!
Query(Story)

# Q 696 : # @invitation_requests.each
Query(InvitationRequest)

# Q 697 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 698 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 699 : # @invitation.user
Query(User)
.where("id = ?")
# Q 700 : # self.find_or_create_key_for_update(key, value)
Query(Keystore)

# Q 701 : # self.find_or_create_key_for_update(key, value)
Query(Keystore)

# Q 702 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 703 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 704 : # HatRequest.new
Query(HatRequest)

# Q 705 : # HatRequest.new
Query(HatRequest)

# Q 706 : # HatRequest.new
Query(HatRequest)

# Q 707 : # @user.undeleted_sent_messages
Query(User)

# Q 708 : # @user.undeleted_sent_messages
Query(User)

# Q 709 : # @user.undeleted_sent_messages
Query(User)

# Q 710 : # Keystore.transaction
Query(Keystore)

# Q 711 : # Keystore.transaction
Query(Keystore)

# Q 712 : # User.make!(:password => "hunter2")
Query(User)

# Q 713 : # User.make!
Query(User)

# Q 714 : # User.make!(:password => "hunter2")
Query(User)

# Q 715 : # User.make!
Query(User)

# Q 716 : # User.make!(:password => "hunter2")
Query(User)

# Q 717 : # User.make!
Query(User)

# Q 718 : # User.make!
Query(User)

# Q 719 : # Story.make!(:title => "hello")
Query(Story)

# Q 720 : # Story.make!
Query(Story)

# Q 721 : # Story.make!(:title => "hello")
Query(Story)

# Q 722 : # Story.make!
Query(Story)

# Q 723 : # Story.make!(:title => "hello")
Query(Story)

# Q 724 : # Story.make!(:title => "hello")
Query(Story)

# Q 725 : # Story.make!
Query(Story)

# Q 726 : # Story.make!(:title => "hello")
Query(Story)

# Q 727 : # Story.make!
Query(Story)

# Q 728 : # @message.author_username
Query(Message)

# Q 729 : # user.is_new?
Query(User)

# Q 730 : # @story.story_cache
Query(Story)
.select('story_cache')
# Q 731 : # story.is_gone?
Query(Story)

# Q 732 : # Tagging.group(:tag_id).count
Query(Tagging)
.group('tag_id')
# Q 733 : # Tagging.group(:tag_id).count
Query(Tagging)
.group('tag_id')
# Q 734 : # Tagging.group(:tag_id)
Query(Tagging)
.group('tag_id')
# Q 735 : # Tagging.group
Query(Tagging)
.group('')
# Q 736 : # Tagging.group(:tag_id).count
Query(Tagging)
.group('tag_id')
# Q 737 : # Tagging.group
Query(Tagging)
.group('')
# Q 738 : # self.hat.gsub(/[^A-Za-z0-9]/, "_").downcase
Query(Hat)
.select('hat')
# Q 739 : # self.hat.gsub(/[^A-Za-z0-9]/, "_")
Query(Hat)
.select('hat')
# Q 740 : # self.hat.gsub
Query(Hat)
.select('hat')
# Q 741 : # self.hat
Query(Hat)
.select('hat')
# Q 742 : # self.hat.gsub(/[^A-Za-z0-9]/, "_").downcase
Query(Hat)
.select('hat')
# Q 743 : # self.hat.gsub
Query(Hat)
.select('hat')
# Q 744 : # self.hat
Query(Hat)
.select('hat')
# Q 745 : # @user.id
Query(User)

# Q 746 : # @user.id
Query(User)

# Q 747 : # @user.id
Query(User)

# Q 748 : # @users.length
Query(User)

# Q 749 : # @users.length
Query(User)

# Q 750 : # @users.length
Query(User)

# Q 751 : # User.make!
Query(User)

# Q 752 : # u = User.make!
Query(User)

# Q 753 : # u = User.make!
Query(User)

# Q 754 : # User.make!
Query(User)

# Q 755 : # story.taggings.each do |tagging|
#   
#   
#   tagging.tag.tag
# end
Query(Tagging)
.where("story_id = ?")
# Q 756 : # story.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 757 : # story.taggings
Query(Tagging)
.where("story_id = ?")
# Q 758 : # @messages.any?
Query(Message)

# Q 759 : # story.is_moderated?
Query(Story)

# Q 760 : # self.action
Query(Moderation)
.select('action')
# Q 761 : # self.action
Query(Moderation)
.select('action')
# Q 762 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 763 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 764 : # ShortId.new(self.class)
Query(ShortId)

# Q 765 : # ShortId.new
Query(ShortId)

# Q 766 : # self.class
Query(Message)

# Q 767 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 768 : # ShortId.new
Query(ShortId)

# Q 769 : # self.class
Query(Message)

# Q 770 : # self.granted_by_user.username
Query(User)
.where("id = ?")
.select('username')
# Q 771 : # self.granted_by_user
Query(User)
.where("id = ?")
# Q 772 : # self.granted_by_user.username
Query(User)
.where("id = ?")
.select('username')
# Q 773 : # self.granted_by_user
Query(User)
.where("id = ?")
# Q 774 : # Message.new
Query(Message)

# Q 775 : # Message.new
Query(Message)

# Q 776 : # Message.new
Query(Message)

# Q 777 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 778 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 779 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 780 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 781 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 782 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 783 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 784 : # @search.what
Query(Search)

# Q 785 : # self.memo
Query(InvitationRequest)
.select('memo')
# Q 786 : # self.memo
Query(InvitationRequest)
.select('memo')
# Q 787 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 788 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 789 : # Tag.active.order(:tag)
Query(Tag)
.order('tag')
# Q 790 : # Tag.active.order
Query(Tag)

# Q 791 : # Tag.active
Query(Tag)

# Q 792 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 793 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 794 : # Tag.active.order
Query(Tag)

# Q 795 : # Tag.active
Query(Tag)

# Q 796 : # self.created_at.strftime("%Y-%m-%d")
Query(Hat)
.select('created_at')
# Q 797 : # self.created_at.strftime
Query(Hat)
.select('created_at')
# Q 798 : # self.created_at
Query(Hat)
.select('created_at')
# Q 799 : # self.created_at.strftime
Query(Hat)
.select('created_at')
# Q 800 : # self.created_at
Query(Hat)
.select('created_at')
# Q 801 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id]).first
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 802 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id]).first
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 803 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id])
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
# Q 804 : # story.id
Query(Story)

# Q 805 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id]).first
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 806 : # story.id
Query(Story)

# Q 807 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 808 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 809 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 810 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 811 : # @message.recipient
Query(User)
.where("id = ?")
# Q 812 : # @tags.each do |tag|
#   
#   
#   check_box_tag "tags[]", tag.tag, @filtered_tags.include?(tag)
#   link_to tag.tag, tag_path(tag), :class => tag.css_class
#   tag.description
#   if tag.hotness_mod != 0
#     
#     
#     tag.hotness_mod > 0 ? "+" : ""
#     tag.hotness_mod
#   end
#   tag.stories_count
# end
Query(Tag)

# Q 813 : # @tags.each
Query(Tag)

# Q 814 : # if @user.is_moderator?
#   
#   
#   ir.email
# end
Query(User)

# Q 815 : # @user.is_moderator?
Query(User)

# Q 816 : # user.username
Query(User)
.select('username')
# Q 817 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 818 : # self.reason
Query(Moderation)
.select('reason')
# Q 819 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 820 : # self.reason
Query(Moderation)
.select('reason')
# Q 821 : # self.destroy
Query(HatRequest)

# Q 822 : # self.destroy
Query(HatRequest)

# Q 823 : # self.destroy
Query(HatRequest)

# Q 824 : # Vote.where(:user_id => user, :story_id => stories, :comment_id => nil).each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 825 : # Vote.where(:user_id => user, :story_id => stories, :comment_id => nil)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 826 : # Vote.where(:user_id => user, :story_id => stories, :comment_id => nil).each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 827 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 828 : # Story.make!
Query(Story)

# Q 829 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 830 : # Story.make!
Query(Story)

# Q 831 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 832 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 833 : # Story.make!
Query(Story)

# Q 834 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 835 : # Story.make!
Query(Story)

# Q 836 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 837 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 838 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 839 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 840 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 841 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 842 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 843 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 844 : # @message.recipient
Query(User)
.where("id = ?")
# Q 845 : # user.is_admin?
Query(User)

# Q 846 : # @story.user_id
Query(Story)
.select('user_id')
# Q 847 : # @user.id
Query(User)

# Q 848 : # @story.user_id
Query(Story)
.select('user_id')
# Q 849 : # @user.id
Query(User)

# Q 850 : # self.link.present?
Query(Hat)
.select('link')
# Q 851 : # self.link
Query(Hat)
.select('link')
# Q 852 : # self.link.present?
Query(Hat)
.select('link')
# Q 853 : # self.link
Query(Hat)
.select('link')
# Q 854 : # User.order("id DESC").to_a
Query(User)
.order('id')
.order('id')
# Q 855 : # User.order("id DESC").to_a
Query(User)
.order('id')
.order('id')
# Q 856 : # User.order("id DESC")
Query(User)
.order('id')
.order('id')
# Q 857 : # User.order
Query(User)

# Q 858 : # User.order("id DESC").to_a
Query(User)
.order('id')
.order('id')
# Q 859 : # User.order
Query(User)

# Q 860 : # @message.created_at
Query(Message)
.select('created_at')
# Q 861 : # tag.tag
Query(Tag)
.select('tag')
# Q 862 : # tag.tag
Query(Tag)
.select('tag')
# Q 863 : # tag.tag
Query(Tag)
.select('tag')
# Q 864 : # story.markeddown_description.present?
Query(Story)
.select('markeddown_description')
# Q 865 : # story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 866 : # self.author
Query(User)
.where("id = ?")
# Q 867 : # self.author
Query(User)
.where("id = ?")
# Q 868 : # self.link
Query(Hat)
.select('link')
# Q 869 : # self.link
Query(Hat)
.select('link')
# Q 870 : # Vote.votes_by_user_for_stories_hash(@user.id, scope.map(&:id))
Query(Vote)

# Q 871 : # Vote.votes_by_user_for_stories_hash(@user.id, scope.map(&:id))
Query(Vote)

# Q 872 : # Vote.votes_by_user_for_stories_hash
Query(Vote)

# Q 873 : # @user.id
Query(User)

# Q 874 : # Vote.votes_by_user_for_stories_hash
Query(Vote)

# Q 875 : # @user.id
Query(User)

# Q 876 : # @hat_request.save
Query(HatRequest)

# Q 877 : # @hat_request.save
Query(HatRequest)

# Q 878 : # User.new
Query(User)

# Q 879 : # User.new
Query(User)

# Q 880 : # User.new
Query(User)

# Q 881 : # user.try(:authenticate, params[:password].to_s)
Query(User)
.select('authenticate')
# Q 882 : # user.try
Query(User)

# Q 883 : # user.try
Query(User)

# Q 884 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 885 : # @story.is_editable_by_user?
Query(Story)

# Q 886 : # @story.is_editable_by_user?
Query(Story)

# Q 887 : # users.length
Query(User)

# Q 888 : # users.length
Query(User)

# Q 889 : # users.length
Query(User)

# Q 890 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 891 : # @user.id
Query(User)

# Q 892 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 893 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 894 : # self.comment
Query(Comment)
.select('comment')
# Q 895 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 896 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 897 : # self.comment
Query(Comment)
.select('comment')
# Q 898 : # self.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 899 : # self.author
Query(User)
.where("id = ?")
# Q 900 : # self.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 901 : # self.author
Query(User)
.where("id = ?")
# Q 902 : # @invitation.email
Query(Invitation)
.select('email')
# Q 903 : # @invitation.email
Query(Invitation)
.select('email')
# Q 904 : # @invitation.email
Query(Invitation)
.select('email')
# Q 905 : # users.group_by(&:invited_by_user_id)
Query(User)

# Q 906 : # users.group_by(&:invited_by_user_id)
Query(User)

# Q 907 : # users.group_by
Query(User)

# Q 908 : # users.group_by
Query(User)

# Q 909 : # tag.tag
Query(Tag)
.select('tag')
# Q 910 : # tag.css_class
Query(Tag)

# Q 911 : # tag.tag
Query(Tag)
.select('tag')
# Q 912 : # tag.css_class
Query(Tag)

# Q 913 : # tag.tag
Query(Tag)
.select('tag')
# Q 914 : # tag.css_class
Query(Tag)

# Q 915 : # user.karma
Query(User)
.select('karma')
# Q 916 : # User.username_regex
Query(User)

# Q 917 : # User.username_regex
Query(User)

# Q 918 : # story.comments_path
Query(Story)

# Q 919 : # self.reason
Query(Moderation)
.select('reason')
# Q 920 : # self.reason
Query(Moderation)
.select('reason')
# Q 921 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map(&:story_id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 922 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map(&:story_id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 923 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 924 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id))
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 925 : # @user.id
Query(User)

# Q 926 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 927 : # @user.id
Query(User)

# Q 928 : # User.order("id DESC").limit(10)
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 929 : # User.order("id DESC").limit(10)
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 930 : # User.order("id DESC").limit
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 931 : # User.order("id DESC")
Query(User)
.order('id')
.order('id')
# Q 932 : # User.order
Query(User)

# Q 933 : # User.order("id DESC").limit
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 934 : # User.order
Query(User)

# Q 935 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 936 : # Story.make!
Query(Story)

# Q 937 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 938 : # Story.make!
Query(Story)

# Q 939 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 940 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 941 : # Story.make!
Query(Story)

# Q 942 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 943 : # Story.make!
Query(Story)

# Q 944 : # tag.description
Query(Tag)
.select('description')
# Q 945 : # tag.description
Query(Tag)
.select('description')
# Q 946 : # tag.description
Query(Tag)
.select('description')
# Q 947 : # user.is_moderator?
Query(User)

# Q 948 : # self.transaction
Query(HatRequest)

# Q 949 : # self.transaction
Query(HatRequest)

# Q 950 : # self.incremented_value_for(key, amount)
Query(Keystore)

# Q 951 : # self.incremented_value_for
Query(Keystore)

# Q 952 : # self.incremented_value_for
Query(Keystore)

# Q 953 : # self.send(p).to_s
Query(Search)

# Q 954 : # self.send(p)
Query(Search)

# Q 955 : # self.send
Query(Search)

# Q 956 : # self.send(p).to_s
Query(Search)

# Q 957 : # self.send
Query(Search)

# Q 958 : # Invitation.new
Query(Invitation)

# Q 959 : # Invitation.new
Query(Invitation)

# Q 960 : # Invitation.new
Query(Invitation)

# Q 961 : # User.make!(:username => "admin")
Query(User)

# Q 962 : # User.make!
Query(User)

# Q 963 : # User.make!(:username => "admin")
Query(User)

# Q 964 : # User.make!
Query(User)

# Q 965 : # User.make!(:username => "admin")
Query(User)

# Q 966 : # User.make!(:username => "admin")
Query(User)

# Q 967 : # User.make!
Query(User)

# Q 968 : # User.make!(:username => "admin")
Query(User)

# Q 969 : # User.make!
Query(User)

# Q 970 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 971 : # Story.make!
Query(Story)

# Q 972 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 973 : # Story.make!
Query(Story)

# Q 974 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 975 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 976 : # Story.make!
Query(Story)

# Q 977 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 978 : # Story.make!
Query(Story)

# Q 979 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 980 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 981 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 982 : # @search.order
Query(Search)

# Q 983 : # story.can_be_seen_by_user?
Query(Story)

# Q 984 : # self.tag
Query(Tag)
.select('tag')
# Q 985 : # self.is_media?
Query(Tag)

# Q 986 : # self.tag
Query(Tag)
.select('tag')
# Q 987 : # self.is_media?
Query(Tag)

# Q 988 : # self.user_id.blank? && errors.add(:user_id, "cannot be blank.")
Query(Comment)

# Q 989 : # self.user_id.blank?
Query(Comment)
.select('user_id')
# Q 990 : # self.user_id
Query(Comment)
.select('user_id')
# Q 991 : # Message.new
Query(Message)

# Q 992 : # Message.new
Query(Message)

# Q 993 : # m = Message.new
Query(Message)

# Q 994 : # Message.new
Query(Message)

# Q 995 : # user.is_banned?
Query(User)

# Q 996 : # user.is_banned?
Query(User)

# Q 997 : # @user.id
Query(User)

# Q 998 : # @user.id
Query(User)

# Q 999 : # @user.id
Query(User)

# Q 1000 : # @message.linkified_body
Query(Message)

# Q 1001 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1002 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1003 : # user.id
Query(User)

# Q 1004 : # user.id
Query(User)

# Q 1005 : # user.id
Query(User)

# Q 1006 : # user.id
Query(User)

# Q 1007 : # user.id
Query(User)

# Q 1008 : # Message.new(message_params)
Query(Message)

# Q 1009 : # Message.new(message_params)
Query(Message)

# Q 1010 : # Message.new
Query(Message)

# Q 1011 : # Message.new
Query(Message)

# Q 1012 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 1013 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 1014 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token)
Query(User)
.where(" = ?")
# Q 1015 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 1016 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1017 : # Story.make!
Query(Story)

# Q 1018 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1019 : # Story.make!
Query(Story)

# Q 1020 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1021 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1022 : # Story.make!
Query(Story)

# Q 1023 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1024 : # Story.make!
Query(Story)

# Q 1025 : # comment.new_record?
Query(Comment)

# Q 1026 : # comment.new_record? ? "Post" : "Update"
Query(Comment)

# Q 1027 : # comment.new_record?
Query(Comment)

# Q 1028 : # @messages.includes(:author, :recipient).each do |message|
#   
#   
#   message.has_been_read? ? "" : "bold"
#   check_box_tag "delete_#{
#   message.short_id}"
#   if @direction == :in
#     
#     if message.author
#       
#       
#       message.author.username
#       message.author.username
#     else
#       
#       
#       message.author_username
#     end
#   else
#     
#     
#     message.recipient.username
#     message.recipient.username
#   end
#   time_ago_in_words_label(message.created_at)
#   message.short_id
#   message.subject
# end
Query(Message)
.includes('author')
.includes('recipient')
# Q 1029 : # @messages.includes(:author, :recipient).each
Query(Message)
.includes('author')
.includes('recipient')
# Q 1030 : # @messages.includes
Query(Message)

# Q 1031 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1032 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1033 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1034 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1035 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1036 : # story.sorted_taggings.each
Query(Story)

# Q 1037 : # story.sorted_taggings
Query(Story)

# Q 1038 : # @story.previewing
Query(Story)

# Q 1039 : # @story.valid?
Query(Story)

# Q 1040 : # self.comment.user_id
Query(Comment)
.where("id = ?")
.select('user_id')
# Q 1041 : # self.comment.user_id
Query(Comment)
.where("id = ?")
.select('user_id')
# Q 1042 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1043 : # self.comment.user_id
Query(Comment)
.where("id = ?")
.select('user_id')
# Q 1044 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1045 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 1046 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 1047 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 1048 : # @user.id
Query(User)

# Q 1049 : # @user.id
Query(User)

# Q 1050 : # @user.id
Query(User)

# Q 1051 : # user.is_active?
Query(User)

# Q 1052 : # user.is_active?
Query(User)

# Q 1053 : # message.has_been_read? ? "" : "bold"
Query(Message)

# Q 1054 : # message.has_been_read? ? "" : "bold"
Query(Message)

# Q 1055 : # message.has_been_read?
Query(Message)

# Q 1056 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1057 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1058 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1059 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1060 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1061 : # user.id
Query(User)

# Q 1062 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1063 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1064 : # self.story_id.blank? && errors.add(:story_id, "cannot be blank.")
Query(Comment)

# Q 1065 : # self.story_id.blank?
Query(Comment)
.select('story_id')
# Q 1066 : # self.story_id
Query(Comment)
.select('story_id')
# Q 1067 : # self.link
Query(Hat)
.select('link')
# Q 1068 : # self.link
Query(Hat)
.select('link')
# Q 1069 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1070 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1071 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1072 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1073 : # Keystore.transaction
Query(Keystore)

# Q 1074 : # Keystore.transaction
Query(Keystore)

# Q 1075 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 1076 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 1077 : # Invitation.where(:code => params[:invitation_code].to_s)
Query(Invitation)
.where("code = ?")
# Q 1078 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 1079 : # User.make!(:banned)
Query(User)

# Q 1080 : # User.make!
Query(User)

# Q 1081 : # User.make!(:banned)
Query(User)

# Q 1082 : # User.make!
Query(User)

# Q 1083 : # User.make!(:banned)
Query(User)

# Q 1084 : # User.make!
Query(User)

# Q 1085 : # User.make!
Query(User)

# Q 1086 : # @user.show_avatars?
Query(User)

# Q 1087 : # message.short_id
Query(Message)
.select('short_id')
# Q 1088 : # message.short_id
Query(Message)
.select('short_id')
# Q 1089 : # message.short_id
Query(Message)
.select('short_id')
# Q 1090 : # message.short_id
Query(Message)
.select('short_id')
# Q 1091 : # message.short_id
Query(Message)
.select('short_id')
# Q 1092 : # if @user.is_moderator?
#   
#   
#   form_tag delete_invitation_request_path do
#     
#     
#     hidden_field_tag "code", ir.code
#     submit_tag "Delete", :data => { :confirm => "Are you sure " << "you want to delete this request?" }
#   end
# end
Query(User)

# Q 1093 : # @user.is_moderator?
Query(User)

# Q 1094 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1095 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1096 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1097 : # self.privileged?
Query(Tag)

# Q 1098 : # self.privileged?
Query(Tag)

# Q 1099 : # self.comment.story.title
Query(Story)
.where("id = ?")
.where("id = ?")
.select('title')
# Q 1100 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1101 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1102 : # self.comment.story.title
Query(Story)
.where("id = ?")
.where("id = ?")
.select('title')
# Q 1103 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1104 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1105 : # self.deleted_by_author?
Query(Message)

# Q 1106 : # self.deleted_by_recipient?
Query(Message)

# Q 1107 : # self.deleted_by_author?
Query(Message)

# Q 1108 : # self.deleted_by_recipient?
Query(Message)

# Q 1109 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1110 : # Keystore.connection
Query(Keystore)

# Q 1111 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1112 : # Keystore.connection
Query(Keystore)

# Q 1113 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1114 : # Keystore.connection
Query(Keystore)

# Q 1115 : # self.total_results.to_i
Query(Search)

# Q 1116 : # self.total_results.to_i
Query(Search)

# Q 1117 : # self.total_results
Query(Search)

# Q 1118 : # self.total_results.to_i
Query(Search)

# Q 1119 : # self.total_results
Query(Search)

# Q 1120 : # user.is_active?
Query(User)

# Q 1121 : # user.is_active?
Query(User)

# Q 1122 : # @story.user_id
Query(Story)
.select('user_id')
# Q 1123 : # @user.id
Query(User)

# Q 1124 : # @story.user_id
Query(Story)
.select('user_id')
# Q 1125 : # @user.id
Query(User)

# Q 1126 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id).first
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
.return_limit('1')
# Q 1127 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id).first
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
.return_limit('1')
# Q 1128 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id)
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
# Q 1129 : # story.id
Query(Story)

# Q 1130 : # @user.id
Query(User)

# Q 1131 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id).first
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
.return_limit('1')
# Q 1132 : # story.id
Query(Story)

# Q 1133 : # @user.id
Query(User)

# Q 1134 : # User.make!
Query(User)

# Q 1135 : # user = User.make!
Query(User)

# Q 1136 : # user = User.make!
Query(User)

# Q 1137 : # User.make!
Query(User)

# Q 1138 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1139 : # comment.user
Query(User)
.where("id = ?")
# Q 1140 : # @search.order
Query(Search)

# Q 1141 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1142 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1143 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1144 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1145 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1146 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1147 : # user.try(:is_moderator?)
Query(User)
.select('is_moderator?')
# Q 1148 : # user.try
Query(User)

# Q 1149 : # user.try
Query(User)

# Q 1150 : # self.comment.story.comments_url
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1151 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1152 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1153 : # self.comment.story.comments_url
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1154 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1155 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1156 : # self.destroy
Query(Message)

# Q 1157 : # self.destroy
Query(Message)

# Q 1158 : # Vote.where(:user_id => user_id, :story_id => story_id).where("comment_id IS NOT NULL").each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where(" = ?")
# Q 1159 : # Vote.where(:user_id => user_id, :story_id => story_id).where("comment_id IS NOT NULL")
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where(" = ?")
# Q 1160 : # Vote.where(:user_id => user_id, :story_id => story_id).where
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
# Q 1161 : # Vote.where(:user_id => user_id, :story_id => story_id)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
# Q 1162 : # Vote.where(:user_id => user_id, :story_id => story_id).where("comment_id IS NOT NULL").each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where(" = ?")
# Q 1163 : # Vote.where(:user_id => user_id, :story_id => story_id).where
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
# Q 1164 : # Keystore.connection.execute
Query(Keystore)

# Q 1165 : # Keystore.connection
Query(Keystore)

# Q 1166 : # Keystore.connection.execute
Query(Keystore)

# Q 1167 : # Keystore.connection
Query(Keystore)

# Q 1168 : # Keystore.connection.execute
Query(Keystore)

# Q 1169 : # Keystore.connection
Query(Keystore)

# Q 1170 : # user.undelete!
Query(User)

# Q 1171 : # user.undelete!
Query(User)

# Q 1172 : # @user.undeleted_received_messages
Query(User)

# Q 1173 : # @user.undeleted_received_messages
Query(User)

# Q 1174 : # @user.undeleted_received_messages
Query(User)

# Q 1175 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1176 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1177 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1178 : # Story.make!
Query(Story)

# Q 1179 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1180 : # Story.make!
Query(Story)

# Q 1181 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1182 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1183 : # Story.make!
Query(Story)

# Q 1184 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1185 : # Story.make!
Query(Story)

# Q 1186 : # Story.make!
Query(Story)

# Q 1187 : # s = Story.make!
Query(Story)

# Q 1188 : # s = Story.make!
Query(Story)

# Q 1189 : # Story.make!
Query(Story)

# Q 1190 : # comment.user.avatar_url
Query(User)
.where("id = ?")
# Q 1191 : # comment.user
Query(User)
.where("id = ?")
# Q 1192 : # message.author
Query(User)
.where("id = ?")
# Q 1193 : # if message.author
#   
#   
#   message.author.username
#   message.author.username
# else
#   
#   
#   message.author_username
# end
Query(Message)

# Q 1194 : # message.author
Query(User)
.where("id = ?")
# Q 1195 : # if message.author
#   
#   
#   message.author.username
#   message.author.username
# else
#   
#   
#   message.author_username
# end
Query(Message)

# Q 1196 : # message.author
Query(User)
.where("id = ?")
# Q 1197 : # tag.stories_count
Query(Tag)

# Q 1198 : # tag.stories_count
Query(Tag)

# Q 1199 : # tag.stories_count
Query(Tag)

# Q 1200 : # @story.previewing
Query(Story)

# Q 1201 : # self.comment.to_s.strip.match(/\A(t)his([\.!])?$\z/i)
Query(Comment)
.select('comment')
# Q 1202 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1203 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1204 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1205 : # self.comment
Query(Comment)
.select('comment')
# Q 1206 : # self.comment.to_s.strip.match(/\A(t)his([\.!])?$\z/i)
Query(Comment)
.select('comment')
# Q 1207 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1208 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1209 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1210 : # self.comment
Query(Comment)
.select('comment')
# Q 1211 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1212 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1213 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1214 : # self.comment
Query(Comment)
.select('comment')
# Q 1215 : # self.hat
Query(Hat)
.select('hat')
# Q 1216 : # self.hat
Query(Hat)
.select('hat')
# Q 1217 : # Keystore.table_name
Query(Keystore)

# Q 1218 : # Keystore.table_name
Query(Keystore)

# Q 1219 : # Keystore.table_name
Query(Keystore)

# Q 1220 : # Keystore.table_name
Query(Keystore)

# Q 1221 : # self.max_matches
Query(Search)

# Q 1222 : # self.max_matches
Query(Search)

# Q 1223 : # user.is_banned?.should
Query(User)

# Q 1224 : # user.is_banned?
Query(User)

# Q 1225 : # user.is_banned?.should == false
Query(User)

# Q 1226 : # user.is_banned?.should == false
Query(User)

# Q 1227 : # user.is_banned?.should
Query(User)

# Q 1228 : # user.is_banned?
Query(User)

# Q 1229 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1230 : # message.author
Query(User)
.where("id = ?")
# Q 1231 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1232 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1233 : # message.author
Query(User)
.where("id = ?")
# Q 1234 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1235 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1236 : # message.author
Query(User)
.where("id = ?")
# Q 1237 : # self.comment.comment
Query(Comment)
.where("id = ?")
.select('comment')
# Q 1238 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1239 : # self.comment.comment
Query(Comment)
.where("id = ?")
.select('comment')
# Q 1240 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1241 : # self.destroy
Query(HatRequest)

# Q 1242 : # self.destroy
Query(HatRequest)

# Q 1243 : # self.destroy
Query(HatRequest)

# Q 1244 : # self.max_matches
Query(Search)

# Q 1245 : # self.max_matches
Query(Search)

# Q 1246 : # self.max_matches
Query(Search)

# Q 1247 : # HatRequest.all.includes(:user)
Query(HatRequest)
.includes('user')
# Q 1248 : # HatRequest.all.includes(:user)
Query(HatRequest)
.includes('user')
# Q 1249 : # HatRequest.all.includes
Query(HatRequest)

# Q 1250 : # HatRequest.all
Query(HatRequest)

# Q 1251 : # HatRequest.all.includes
Query(HatRequest)

# Q 1252 : # HatRequest.all
Query(HatRequest)

# Q 1253 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1254 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1255 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 1256 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1257 : # comment.errors.add(:comment, "^You have already posted a comment " << "here recently.")
Query(Comment)

# Q 1258 : # comment.errors.add
Query(Comment)

# Q 1259 : # comment.errors
Query(Comment)

# Q 1260 : # comment.errors.add
Query(Comment)

# Q 1261 : # comment.errors
Query(Comment)

# Q 1262 : # User.exists?(:username => u[1..-1])
Query(User)
.return_limit('1')
# Q 1263 : # User.exists?
Query(User)
.return_limit('1')
# Q 1264 : # User.exists?(:username => u[1..-1])
Query(User)
.return_limit('1')
# Q 1265 : # User.exists?
Query(User)
.return_limit('1')
# Q 1266 : # User.exists?(:username => u[1..-1])
Query(User)
.return_limit('1')
# Q 1267 : # User.exists?
Query(User)
.return_limit('1')
# Q 1268 : # User.exists?(:username => u[1..-1])
Query(User)
.return_limit('1')
# Q 1269 : # User.exists?
Query(User)
.return_limit('1')
# Q 1270 : # User.exists?
Query(User)
.return_limit('1')
# Q 1271 : # comment.persisted?
Query(Comment)

# Q 1272 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1273 : # comment.persisted?
Query(Comment)

# Q 1274 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1275 : # @message.short_id
Query(Message)
.select('short_id')
# Q 1276 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1277 : # message.author
Query(User)
.where("id = ?")
# Q 1278 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1279 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1280 : # message.author
Query(User)
.where("id = ?")
# Q 1281 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1282 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1283 : # message.author
Query(User)
.where("id = ?")
# Q 1284 : # @story.is_gone?
Query(Story)

# Q 1285 : # @story.previewing
Query(Story)

# Q 1286 : # story.domain.present?
Query(Story)

# Q 1287 : # story.domain
Query(Story)

# Q 1288 : # Keystore.connection.execute
Query(Keystore)

# Q 1289 : # Keystore.connection
Query(Keystore)

# Q 1290 : # Keystore.table_name
Query(Keystore)

# Q 1291 : # Keystore.connection.execute
Query(Keystore)

# Q 1292 : # Keystore.connection
Query(Keystore)

# Q 1293 : # Keystore.table_name
Query(Keystore)

# Q 1294 : # Keystore.table_name
Query(Keystore)

# Q 1295 : # Keystore.connection.execute
Query(Keystore)

# Q 1296 : # Keystore.connection
Query(Keystore)

# Q 1297 : # Keystore.table_name
Query(Keystore)

# Q 1298 : # @story.save(:validate => false)
Query(Story)

# Q 1299 : # @story.save
Query(Story)

# Q 1300 : # @story.save
Query(Story)

# Q 1301 : # stories.hidden
Query(Story)

# Q 1302 : # stories.hidden
Query(Story)

# Q 1303 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1304 : # Story.make!
Query(Story)

# Q 1305 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1306 : # Story.make!
Query(Story)

# Q 1307 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1308 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1309 : # Story.make!
Query(Story)

# Q 1310 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1311 : # Story.make!
Query(Story)

# Q 1312 : # User.make!
Query(User)

# Q 1313 : # u = User.make!
Query(User)

# Q 1314 : # u = User.make!
Query(User)

# Q 1315 : # User.make!
Query(User)

# Q 1316 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1317 : # comment.user
Query(User)
.where("id = ?")
# Q 1318 : # story.domain_search_url
Query(Story)

# Q 1319 : # @story.previewing
Query(Story)

# Q 1320 : # self.comment.to_s.strip.match(/\Atl;?dr.?$\z/i)
Query(Comment)
.select('comment')
# Q 1321 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1322 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1323 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1324 : # self.comment
Query(Comment)
.select('comment')
# Q 1325 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1326 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1327 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1328 : # self.comment
Query(Comment)
.select('comment')
# Q 1329 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 1330 : # self.reason
Query(Moderation)
.select('reason')
# Q 1331 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 1332 : # self.reason
Query(Moderation)
.select('reason')
# Q 1333 : # comment.html_class_for_user
Query(Comment)

# Q 1334 : # message.author_username
Query(Message)

# Q 1335 : # message.author_username
Query(Message)

# Q 1336 : # message.author_username
Query(Message)

# Q 1337 : # message.author_username
Query(Message)

# Q 1338 : # message.author_username
Query(Message)

# Q 1339 : # @search.order
Query(Search)

# Q 1340 : # story.domain
Query(Story)

# Q 1341 : # self.recipient.update_unread_message_count!
Query(User)
.where("id = ?")
# Q 1342 : # self.recipient
Query(User)
.where("id = ?")
# Q 1343 : # self.recipient.update_unread_message_count!
Query(User)
.where("id = ?")
# Q 1344 : # self.recipient
Query(User)
.where("id = ?")
# Q 1345 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1346 : # Keystore.connection
Query(Keystore)

# Q 1347 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1348 : # Keystore.connection
Query(Keystore)

# Q 1349 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1350 : # Keystore.connection
Query(Keystore)

# Q 1351 : # self.per_page.to_i
Query(Search)

# Q 1352 : # self.per_page
Query(Search)

# Q 1353 : # self.per_page.to_i
Query(Search)

# Q 1354 : # self.per_page
Query(Search)

# Q 1355 : # User.new(user_params)
Query(User)

# Q 1356 : # User.new(user_params)
Query(User)

# Q 1357 : # User.new
Query(User)

# Q 1358 : # User.new
Query(User)

# Q 1359 : # user.session_token
Query(User)
.select('session_token')
# Q 1360 : # user.session_token
Query(User)
.select('session_token')
# Q 1361 : # user.session_token
Query(User)
.select('session_token')
# Q 1362 : # @story.comments_path
Query(Story)

# Q 1363 : # @story.comments_path
Query(Story)

# Q 1364 : # User.make!(:banned)
Query(User)

# Q 1365 : # User.make!
Query(User)

# Q 1366 : # User.make!(:banned)
Query(User)

# Q 1367 : # User.make!
Query(User)

# Q 1368 : # User.make!(:banned)
Query(User)

# Q 1369 : # User.make!
Query(User)

# Q 1370 : # User.make!
Query(User)

# Q 1371 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, nil, u.id, "H")
Query(Vote)

# Q 1372 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1373 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, nil, u.id, "H")
Query(Vote)

# Q 1374 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, nil, u.id, "H")
Query(Vote)

# Q 1375 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1376 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1377 : # comment.user
Query(User)
.where("id = ?")
# Q 1378 : # Keystore.connection.execute
Query(Keystore)

# Q 1379 : # Keystore.connection
Query(Keystore)

# Q 1380 : # Keystore.table_name
Query(Keystore)

# Q 1381 : # Keystore.connection.execute
Query(Keystore)

# Q 1382 : # Keystore.connection
Query(Keystore)

# Q 1383 : # Keystore.table_name
Query(Keystore)

# Q 1384 : # Keystore.table_name
Query(Keystore)

# Q 1385 : # Keystore.connection.execute
Query(Keystore)

# Q 1386 : # Keystore.connection
Query(Keystore)

# Q 1387 : # Keystore.table_name
Query(Keystore)

# Q 1388 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1389 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1390 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1391 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1392 : # @invitation.user_id
Query(Invitation)
.select('user_id')
# Q 1393 : # @invitation.user_id
Query(Invitation)
.select('user_id')
# Q 1394 : # @invitation.user_id
Query(Invitation)
.select('user_id')
# Q 1395 : # User.make!
Query(User)

# Q 1396 : # user = User.make!
Query(User)

# Q 1397 : # user = User.make!
Query(User)

# Q 1398 : # User.make!
Query(User)

# Q 1399 : # @comments.group_by
Query(Comment)

# Q 1400 : # TagFilter.where(:tag_id => self.id).count
Query(TagFilter)
.where("tag_id = ?")
# Q 1401 : # TagFilter.where(:tag_id => self.id)
Query(TagFilter)
.where("tag_id = ?")
# Q 1402 : # self.id
Query(Tag)

# Q 1403 : # TagFilter.where(:tag_id => self.id).count
Query(TagFilter)
.where("tag_id = ?")
# Q 1404 : # self.id
Query(Tag)

# Q 1405 : # @hat_request.update_attributes!(params.require(:hat_request).permit(:hat, :link))
Query(HatRequest)

# Q 1406 : # @hat_request.update_attributes!
Query(HatRequest)

# Q 1407 : # @hat_request.update_attributes!
Query(HatRequest)

# Q 1408 : # user.password_digest.to_s.match(/^\$2a\$#{
# BCrypt::Engine::DEFAULT_COST}\$/)
Query(User)
.select('password_digest')
# Q 1409 : # user.password_digest.to_s.match
Query(User)
.select('password_digest')
# Q 1410 : # user.password_digest.to_s
Query(User)
.select('password_digest')
# Q 1411 : # user.password_digest
Query(User)
.select('password_digest')
# Q 1412 : # user.password_digest.to_s.match
Query(User)
.select('password_digest')
# Q 1413 : # user.password_digest.to_s
Query(User)
.select('password_digest')
# Q 1414 : # user.password_digest
Query(User)
.select('password_digest')
# Q 1415 : # comment.hat
Query(Hat)
.where("id = ?")
# Q 1416 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1417 : # message.recipient
Query(User)
.where("id = ?")
# Q 1418 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1419 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1420 : # message.recipient
Query(User)
.where("id = ?")
# Q 1421 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1422 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1423 : # message.recipient
Query(User)
.where("id = ?")
# Q 1424 : # self.reason
Query(Moderation)
.select('reason')
# Q 1425 : # self.reason
Query(Moderation)
.select('reason')
# Q 1426 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC").reject
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1427 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC")
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1428 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1429 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago))
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1430 : # stories.select(:id, :upvotes, :downvotes, :user_id).where
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1431 : # stories.select(:id, :upvotes, :downvotes, :user_id)
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1432 : # stories.select
Query(Story)

# Q 1433 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC").reject
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1434 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC")
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1435 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1436 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago))
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1437 : # stories.select(:id, :upvotes, :downvotes, :user_id).where
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1438 : # stories.select(:id, :upvotes, :downvotes, :user_id)
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1439 : # stories.select
Query(Story)

# Q 1440 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC").reject
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1441 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1442 : # stories.select(:id, :upvotes, :downvotes, :user_id).where
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1443 : # stories.select
Query(Story)

# Q 1444 : # user.is_active?.should
Query(User)

# Q 1445 : # user.is_active?
Query(User)

# Q 1446 : # user.is_active?.should == true
Query(User)

# Q 1447 : # user.is_active?.should == true
Query(User)

# Q 1448 : # user.is_active?.should
Query(User)

# Q 1449 : # user.is_active?
Query(User)

# Q 1450 : # Story.count.should
Query(Story)

# Q 1451 : # Story.count
Query(Story)

# Q 1452 : # Story.count.should == 0
Query(Story)

# Q 1453 : # Story.count.should == 0
Query(Story)

# Q 1454 : # Story.count.should
Query(Story)

# Q 1455 : # Story.count
Query(Story)

# Q 1456 : # @user.hats.any?
Query(Hat)
.where("user_id = ?")
# Q 1457 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1458 : # @user.hats.any?
Query(Hat)
.where("user_id = ?")
# Q 1459 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1460 : # comment.hat.to_html_label
Query(Hat)
.where("id = ?")
# Q 1461 : # comment.hat
Query(Hat)
.where("id = ?")
# Q 1462 : # @message.short_id
Query(Message)
.select('short_id')
# Q 1463 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1464 : # message.recipient
Query(User)
.where("id = ?")
# Q 1465 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1466 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1467 : # message.recipient
Query(User)
.where("id = ?")
# Q 1468 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1469 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1470 : # message.recipient
Query(User)
.where("id = ?")
# Q 1471 : # @invitation_requests.count
Query(InvitationRequest)

# Q 1472 : # story.merged_stories.each
Query(Story)
.where("story_id = ?")
# Q 1473 : # story.merged_stories
Query(Story)
.where("story_id = ?")
# Q 1474 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1475 : # self.order("confidence DESC").group_by(&:parent_comment_id)
Query(Comment)
.order('id')
.order('confidence')
# Q 1476 : # self.order("confidence DESC").group_by(&:parent_comment_id)
Query(Comment)
.order('id')
.order('confidence')
# Q 1477 : # self.order("confidence DESC").group_by
Query(Comment)
.order('id')
.order('confidence')
# Q 1478 : # self.order("confidence DESC")
Query(Comment)
.order('id')
.order('confidence')
# Q 1479 : # self.order
Query(Comment)

# Q 1480 : # self.order("confidence DESC").group_by
Query(Comment)
.order('id')
.order('confidence')
# Q 1481 : # self.order
Query(Comment)

# Q 1482 : # Story.arel_table
Query(Story)

# Q 1483 : # Story.arel_table
Query(Story)

# Q 1484 : # Story.arel_table
Query(Story)

# Q 1485 : # @hat_request.approve_by_user!(@user)
Query(HatRequest)

# Q 1486 : # @hat_request.approve_by_user!
Query(HatRequest)

# Q 1487 : # @hat_request.approve_by_user!
Query(HatRequest)

# Q 1488 : # @invitation.destroy
Query(Invitation)

# Q 1489 : # @invitation.destroy
Query(Invitation)

# Q 1490 : # user.save!
Query(User)

# Q 1491 : # user.save!
Query(User)

# Q 1492 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 1493 : # @story.is_editable_by_user?
Query(Story)

# Q 1494 : # @story.is_editable_by_user?
Query(Story)

# Q 1495 : # Comment.where(:short_id => m[1]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 1496 : # Comment.where(:short_id => m[1]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 1497 : # Comment.where(:short_id => m[1])
Query(Comment)
.where("short_id = ?")
# Q 1498 : # Comment.where(:short_id => m[1]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 1499 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1500 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1501 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1502 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1503 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1504 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1505 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1506 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1507 : # comment.valid?
Query(Comment)

# Q 1508 : # comment.save
Query(Comment)

# Q 1509 : # comment.valid?
Query(Comment)

# Q 1510 : # comment.save
Query(Comment)

# Q 1511 : # Story.make!(:title => "flim flam", :url => "http://example.com/")
Query(Story)

# Q 1512 : # Story.make!
Query(Story)

# Q 1513 : # Story.make!(:title => "flim flam", :url => "http://example.com/")
Query(Story)

# Q 1514 : # Story.make!(:title => "flim flam", :url => "http://example.com/")
Query(Story)

# Q 1515 : # Story.make!
Query(Story)

# Q 1516 : # message.created_at
Query(Message)
.select('created_at')
# Q 1517 : # @user.is_moderator?
Query(User)

# Q 1518 : # self.recipient.email_messages?
Query(User)
.where("id = ?")
# Q 1519 : # self.recipient
Query(User)
.where("id = ?")
# Q 1520 : # self.recipient.email_messages?
Query(User)
.where("id = ?")
# Q 1521 : # self.recipient
Query(User)
.where("id = ?")
# Q 1522 : # self.page
Query(Search)

# Q 1523 : # self.page_count
Query(Search)

# Q 1524 : # self.page
Query(Search)

# Q 1525 : # self.page_count
Query(Search)

# Q 1526 : # Story.where(:short_id => m[1]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 1527 : # Story.where(:short_id => m[1]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 1528 : # Story.where(:short_id => m[1])
Query(Story)
.where("short_id = ?")
# Q 1529 : # Story.where(:short_id => m[1]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 1530 : # Story.count.should
Query(Story)

# Q 1531 : # Story.count
Query(Story)

# Q 1532 : # Story.count.should == 1
Query(Story)

# Q 1533 : # Story.count.should == 1
Query(Story)

# Q 1534 : # Story.count.should
Query(Story)

# Q 1535 : # Story.count
Query(Story)

# Q 1536 : # comment.previewing
Query(Comment)

# Q 1537 : # message.subject
Query(Message)
.select('subject')
# Q 1538 : # message.short_id
Query(Message)
.select('short_id')
# Q 1539 : # message.subject
Query(Message)
.select('subject')
# Q 1540 : # message.short_id
Query(Message)
.select('short_id')
# Q 1541 : # message.short_id
Query(Message)
.select('short_id')
# Q 1542 : # message.subject
Query(Message)
.select('subject')
# Q 1543 : # self.create_rss_token
Query(User)

# Q 1544 : # self.create_rss_token
Query(User)

# Q 1545 : # self.per_page
Query(Search)

# Q 1546 : # self.per_page
Query(Search)

# Q 1547 : # User.make!(:created_at => Time.now)
Query(User)

# Q 1548 : # User.make!
Query(User)

# Q 1549 : # User.make!(:created_at => Time.now)
Query(User)

# Q 1550 : # User.make!
Query(User)

# Q 1551 : # User.make!(:created_at => Time.now)
Query(User)

# Q 1552 : # User.make!
Query(User)

# Q 1553 : # User.make!
Query(User)

# Q 1554 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1555 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1556 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1557 : # self.recipient
Query(User)
.where("id = ?")
# Q 1558 : # self.recipient
Query(User)
.where("id = ?")
# Q 1559 : # Moderation.new
Query(Moderation)

# Q 1560 : # Moderation.new
Query(Moderation)

# Q 1561 : # Moderation.new
Query(Moderation)

# Q 1562 : # self.create_mailing_list_token
Query(User)

# Q 1563 : # self.create_mailing_list_token
Query(User)

# Q 1564 : # @message.subject
Query(Message)
.select('subject')
# Q 1565 : # @message.subject
Query(Message)
.select('subject')
# Q 1566 : # @message.subject
Query(Message)
.select('subject')
# Q 1567 : # User.make!(:created_at => Time.now - 8.days)
Query(User)

# Q 1568 : # User.make!
Query(User)

# Q 1569 : # User.make!(:created_at => Time.now - 8.days)
Query(User)

# Q 1570 : # User.make!
Query(User)

# Q 1571 : # User.make!(:created_at => Time.now - 8.days)
Query(User)

# Q 1572 : # User.make!
Query(User)

# Q 1573 : # User.make!
Query(User)

# Q 1574 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1575 : # Story.make!
Query(Story)

# Q 1576 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1577 : # Story.make!
Query(Story)

# Q 1578 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1579 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1580 : # Story.make!
Query(Story)

# Q 1581 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1582 : # Story.make!
Query(Story)

# Q 1583 : # comment.hat_id
Query(Comment)
.select('hat_id')
# Q 1584 : # comment.hat_id
Query(Comment)
.select('hat_id')
# Q 1585 : # comment.hat_id
Query(Comment)
.select('hat_id')
# Q 1586 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1587 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1588 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1589 : # stories.hottest
Query(Story)

# Q 1590 : # stories.hottest
Query(Story)

# Q 1591 : # user.is_new?.should
Query(User)

# Q 1592 : # user.is_new?
Query(User)

# Q 1593 : # user.is_new?.should == true
Query(User)

# Q 1594 : # user.is_new?.should == true
Query(User)

# Q 1595 : # user.is_new?.should
Query(User)

# Q 1596 : # user.is_new?
Query(User)

# Q 1597 : # Story.make!
Query(Story)

# Q 1598 : # s = Story.make!
Query(Story)

# Q 1599 : # s = Story.make!
Query(Story)

# Q 1600 : # Story.make!
Query(Story)

# Q 1601 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 1602 : # @story.id
Query(Story)

# Q 1603 : # self.recipient.email
Query(User)
.where("id = ?")
.select('email')
# Q 1604 : # self.recipient
Query(User)
.where("id = ?")
# Q 1605 : # self.recipient.email
Query(User)
.where("id = ?")
.select('email')
# Q 1606 : # self.recipient
Query(User)
.where("id = ?")
# Q 1607 : # self.user_id
Query(Hat)
.select('user_id')
# Q 1608 : # self.user_id
Query(Hat)
.select('user_id')
# Q 1609 : # self.user_id
Query(Hat)
.select('user_id')
# Q 1610 : # self.where(:user_id => user_id, :comment_id => nil, :story_id => story_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
.where("story_id = ?")
# Q 1611 : # self.where(:user_id => user_id, :comment_id => nil, :story_id => story_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
.where("story_id = ?")
# Q 1612 : # @message.author
Query(User)
.where("id = ?")
# Q 1613 : # @message.author
Query(User)
.where("id = ?")
# Q 1614 : # @user.save!
Query(User)

# Q 1615 : # @user.save!
Query(User)

# Q 1616 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1617 : # Comment.make!
Query(Comment)

# Q 1618 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1619 : # Comment.make!
Query(Comment)

# Q 1620 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1621 : # Comment.make!
Query(Comment)

# Q 1622 : # Comment.make!
Query(Comment)

# Q 1623 : # comment.has_been_edited?
Query(Comment)

# Q 1624 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 1625 : # @story.id
Query(Story)

# Q 1626 : # self.granted_by_user_id
Query(Hat)
.select('granted_by_user_id')
# Q 1627 : # self.granted_by_user_id
Query(Hat)
.select('granted_by_user_id')
# Q 1628 : # self.granted_by_user_id
Query(Hat)
.select('granted_by_user_id')
# Q 1629 : # self.value_for(key)
Query(Keystore)

# Q 1630 : # self.value_for
Query(Keystore)

# Q 1631 : # self.value_for(key)
Query(Keystore)

# Q 1632 : # self.value_for
Query(Keystore)

# Q 1633 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1634 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1635 : # Message.new
Query(Message)

# Q 1636 : # Message.new
Query(Message)

# Q 1637 : # Message.new
Query(Message)

# Q 1638 : # Story.count.should
Query(Story)

# Q 1639 : # Story.count
Query(Story)

# Q 1640 : # Story.count.should == 1
Query(Story)

# Q 1641 : # Story.count.should == 1
Query(Story)

# Q 1642 : # Story.count.should
Query(Story)

# Q 1643 : # Story.count
Query(Story)

# Q 1644 : # self.hat
Query(Hat)
.select('hat')
# Q 1645 : # self.link.present?
Query(Hat)
.select('link')
# Q 1646 : # self.link
Query(Hat)
.select('link')
# Q 1647 : # self.hat
Query(Hat)
.select('hat')
# Q 1648 : # self.link.present?
Query(Hat)
.select('link')
# Q 1649 : # self.link
Query(Hat)
.select('link')
# Q 1650 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1651 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1652 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1653 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1654 : # @story.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 1655 : # @story.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 1656 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1657 : # @story.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 1658 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1659 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 1660 : # @user.id
Query(User)

# Q 1661 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 1662 : # @user.id
Query(User)

# Q 1663 : # @user.pushover_user_key.present?
Query(User)
.select('pushover_user_key')
# Q 1664 : # @user.pushover_user_key
Query(User)
.select('pushover_user_key')
# Q 1665 : # @user.pushover_user_key.present?
Query(User)
.select('pushover_user_key')
# Q 1666 : # @user.pushover_user_key
Query(User)
.select('pushover_user_key')
# Q 1667 : # comment.is_from_email?
Query(Comment)

# Q 1668 : # comment.id
Query(Comment)

# Q 1669 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1670 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1671 : # self.link
Query(Hat)
.select('link')
# Q 1672 : # self.link
Query(Hat)
.select('link')
# Q 1673 : # @hat_request.reject_by_user_for_reason!(@user, params[:hat_request][:rejection_comment])
Query(HatRequest)

# Q 1674 : # @hat_request.reject_by_user_for_reason!
Query(HatRequest)

# Q 1675 : # @hat_request.reject_by_user_for_reason!
Query(HatRequest)

# Q 1676 : # InvitationRequest.new(params.require(:invitation_request).permit(:name, :email, :memo))
Query(InvitationRequest)

# Q 1677 : # InvitationRequest.new(params.require(:invitation_request).permit(:name, :email, :memo))
Query(InvitationRequest)

# Q 1678 : # InvitationRequest.new
Query(InvitationRequest)

# Q 1679 : # InvitationRequest.new
Query(InvitationRequest)

# Q 1680 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1681 : # @message.recipient
Query(User)
.where("id = ?")
# Q 1682 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1683 : # @message.author
Query(User)
.where("id = ?")
# Q 1684 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1685 : # @message.recipient
Query(User)
.where("id = ?")
# Q 1686 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1687 : # @message.author
Query(User)
.where("id = ?")
# Q 1688 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 1689 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 1690 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1691 : # Story.make!
Query(Story)

# Q 1692 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1693 : # Story.make!
Query(Story)

# Q 1694 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1695 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1696 : # Story.make!
Query(Story)

# Q 1697 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1698 : # Story.make!
Query(Story)

# Q 1699 : # User.make!
Query(User)

# Q 1700 : # u = User.make!
Query(User)

# Q 1701 : # u = User.make!
Query(User)

# Q 1702 : # User.make!
Query(User)

# Q 1703 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1704 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1705 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1706 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1707 : # self.recipient.pushover_messages?
Query(User)
.where("id = ?")
# Q 1708 : # self.recipient
Query(User)
.where("id = ?")
# Q 1709 : # self.recipient.pushover_messages?
Query(User)
.where("id = ?")
# Q 1710 : # self.recipient
Query(User)
.where("id = ?")
# Q 1711 : # User.make!(:banned)
Query(User)

# Q 1712 : # User.make!
Query(User)

# Q 1713 : # User.make!(:banned)
Query(User)

# Q 1714 : # User.make!
Query(User)

# Q 1715 : # User.make!(:banned)
Query(User)

# Q 1716 : # User.make!
Query(User)

# Q 1717 : # User.make!
Query(User)

# Q 1718 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1719 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1720 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1721 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1722 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1723 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1724 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1725 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1726 : # self.recipient.pushover!({ :title => "#{
# Rails.application.name} message from " << "#{
# self.author_username}: #{
# self.subject}", :message => self.plaintext_body, :url => self.url, :url_title => (
# self.author ? "Reply to #{
# self.author_username}" : "View message") })
Query(User)
.where("id = ?")
# Q 1727 : # self.recipient.pushover!
Query(User)
.where("id = ?")
# Q 1728 : # self.recipient
Query(User)
.where("id = ?")
# Q 1729 : # self.recipient.pushover!
Query(User)
.where("id = ?")
# Q 1730 : # self.recipient
Query(User)
.where("id = ?")
# Q 1731 : # votes.inject({ })
Query(Vote)

# Q 1732 : # votes.inject
Query(Vote)

# Q 1733 : # votes.inject
Query(Vote)

# Q 1734 : # @message.subject.match(/^re:/i)
Query(Message)
.select('subject')
# Q 1735 : # @message.subject.match
Query(Message)
.select('subject')
# Q 1736 : # @message.subject
Query(Message)
.select('subject')
# Q 1737 : # @message.subject.match
Query(Message)
.select('subject')
# Q 1738 : # @message.subject
Query(Message)
.select('subject')
# Q 1739 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1740 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1741 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 1742 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1743 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 1744 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 1745 : # User.first
Query(User)
.return_limit('1')
# Q 1746 : # User.first
Query(User)
.return_limit('1')
# Q 1747 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 1748 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1749 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 1750 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 1751 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1752 : # comment.has_been_edited?
Query(Comment)

# Q 1753 : # @message.subject
Query(Message)
.select('subject')
# Q 1754 : # @message.subject
Query(Message)
.select('subject')
# Q 1755 : # @message.subject
Query(Message)
.select('subject')
# Q 1756 : # Story.count.should
Query(Story)

# Q 1757 : # Story.count
Query(Story)

# Q 1758 : # Story.count.should == 1
Query(Story)

# Q 1759 : # Story.count.should == 1
Query(Story)

# Q 1760 : # Story.count.should
Query(Story)

# Q 1761 : # Story.count
Query(Story)

# Q 1762 : # comment.updated_at
Query(Comment)
.select('updated_at')
# Q 1763 : # comment.created_at
Query(Comment)
.select('created_at')
# Q 1764 : # self.author_username
Query(Message)

# Q 1765 : # self.subject
Query(Message)
.select('subject')
# Q 1766 : # self.author_username
Query(Message)

# Q 1767 : # self.subject
Query(Message)
.select('subject')
# Q 1768 : # self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1769 : # self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1770 : # self.lock(true).where(:key => key)
Query(Keystore)
.where("key = ?")
# Q 1771 : # self.lock(true)
Query(Keystore)

# Q 1772 : # self.lock
Query(Keystore)

# Q 1773 : # kv = self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1774 : # self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1775 : # self.lock
Query(Keystore)

# Q 1776 : # Story.new
Query(Story)

# Q 1777 : # Story.new
Query(Story)

# Q 1778 : # Story.new
Query(Story)

# Q 1779 : # self.plaintext_body
Query(Message)

# Q 1780 : # self.plaintext_body
Query(Message)

# Q 1781 : # @invitation_request.save
Query(InvitationRequest)

# Q 1782 : # @invitation_request.save
Query(InvitationRequest)

# Q 1783 : # @message.subject
Query(Message)
.select('subject')
# Q 1784 : # @message.subject
Query(Message)
.select('subject')
# Q 1785 : # self.url
Query(Message)

# Q 1786 : # self.url
Query(Message)

# Q 1787 : # self.q.to_s.split(" ").reject { |w|
#   
#   if m = w.match(/^domain:(.+)$/)
#     
#     domain = m[1]
#   end
# }.join(" ")
Query(Search)

# Q 1788 : # self.q.to_s.split(" ").reject { |w|
#   
#   if m = w.match(/^domain:(.+)$/)
#     
#     domain = m[1]
#   end
# }.join(" ")
Query(Search)

# Q 1789 : # self.q.to_s.split(" ").reject { |w|
#   
#   if m = w.match(/^domain:(.+)$/)
#     
#     domain = m[1]
#   end
# }.join
Query(Search)

# Q 1790 : # self.q.to_s.split(" ").reject
Query(Search)

# Q 1791 : # self.q.to_s.split(" ")
Query(Search)

# Q 1792 : # self.q.to_s.split
Query(Search)

# Q 1793 : # self.q.to_s
Query(Search)

# Q 1794 : # self.q
Query(Search)

# Q 1795 : # self.q.to_s.split(" ").reject { |w|
#   
#   if m = w.match(/^domain:(.+)$/)
#     
#     domain = m[1]
#   end
# }.join
Query(Search)

# Q 1796 : # self.q.to_s.split(" ").reject
Query(Search)

# Q 1797 : # self.q.to_s.split
Query(Search)

# Q 1798 : # self.q.to_s
Query(Search)

# Q 1799 : # self.q
Query(Search)

# Q 1800 : # comment.is_editable_by_user?(@user)
Query(Comment)

# Q 1801 : # comment.is_editable_by_user?
Query(Comment)

# Q 1802 : # comment.is_editable_by_user?
Query(Comment)

# Q 1803 : # comment.previewing
Query(Comment)

# Q 1804 : # self.author
Query(User)
.where("id = ?")
# Q 1805 : # self.author_username
Query(Message)

# Q 1806 : # self.author
Query(User)
.where("id = ?")
# Q 1807 : # self.author_username
Query(Message)

# Q 1808 : # if self.url.present?
#   
#   if self.url.match(/\Ahttps?:\/\/([^\.]+\.)+[a-z]+(\/|\z)/i)
#     
#     if self.new_record? && (
#     s = Story.find_similar_by_url(self.url))
#       
#       self.already_posted_story = s
#       if s.is_recent?
#         
#         errors.add(:url, "has already been submitted within the past " << "#{
#         RECENT_DAYS} days")
#       end
#     end
#   else
#     
#     errors.add(:url, "is not valid")
#   end
# elsif self.description.to_s.strip == ""
#   
#   errors.add(:description, "must contain text if no URL posted")
# end
Query(Story)

# Q 1809 : # self.url.present?
Query(Story)
.select('url')
# Q 1810 : # self.url
Query(Story)
.select('url')
# Q 1811 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1812 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1813 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1814 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1815 : # Story.make!(:url => "http://example.com")
Query(Story)

# Q 1816 : # Story.make!
Query(Story)

# Q 1817 : # Story.make!(:url => "http://example.com")
Query(Story)

# Q 1818 : # Story.make!
Query(Story)

# Q 1819 : # Story.make!(:url => "http://example.com")
Query(Story)

# Q 1820 : # Story.make!
Query(Story)

# Q 1821 : # Story.make!
Query(Story)

# Q 1822 : # self.create!
Query(Keystore)

# Q 1823 : # self.create!
Query(Keystore)

# Q 1824 : # self.create! do |kv|
#   
#   kv.key = key
#   kv.value = init
#   kv.save!
# end
Query(Keystore)

# Q 1825 : # self.create!
Query(Keystore)

# Q 1826 : # comment.short_id_url
Query(Comment)

# Q 1827 : # User.all.each
Query(User)

# Q 1828 : # User.all
Query(User)

# Q 1829 : # User.all.each
Query(User)

# Q 1830 : # User.all
Query(User)

# Q 1831 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 1832 : # @user.id
Query(User)

# Q 1833 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 1834 : # @user.id
Query(User)

# Q 1835 : # @user.show_avatars?
Query(User)

# Q 1836 : # @user && @user.show_avatars?
Query(User)

# Q 1837 : # @user.show_avatars?
Query(User)

# Q 1838 : # user.is_moderator?
Query(User)

# Q 1839 : # user.id
Query(User)

# Q 1840 : # user.is_moderator?
Query(User)

# Q 1841 : # user.id
Query(User)

# Q 1842 : # self.url.match(/\Ahttps?:\/\/([^\.]+\.)+[a-z]+(\/|\z)/i)
Query(Story)
.select('url')
# Q 1843 : # self.url.match
Query(Story)
.select('url')
# Q 1844 : # self.url
Query(Story)
.select('url')
# Q 1845 : # self.url.match
Query(Story)
.select('url')
# Q 1846 : # self.url
Query(Story)
.select('url')
# Q 1847 : # @user.clone
Query(User)

# Q 1848 : # @user.clone
Query(User)

# Q 1849 : # @user.clone
Query(User)

# Q 1850 : # Story.make!(:url => "http://www3.example.com/goose")
Query(Story)

# Q 1851 : # Story.make!
Query(Story)

# Q 1852 : # Story.make!(:url => "http://www3.example.com/goose")
Query(Story)

# Q 1853 : # Story.make!
Query(Story)

# Q 1854 : # Story.make!(:url => "http://www3.example.com/goose")
Query(Story)

# Q 1855 : # Story.make!
Query(Story)

# Q 1856 : # Story.make!
Query(Story)

# Q 1857 : # comment.is_editable_by_user?
Query(Comment)

# Q 1858 : # self.new_record?
Query(Story)

# Q 1859 : # Story.find_similar_by_url(self.url)
Query(Story)

# Q 1860 : # Story.find_similar_by_url
Query(Story)

# Q 1861 : # self.url
Query(Story)
.select('url')
# Q 1862 : # self.new_record?
Query(Story)

# Q 1863 : # Story.find_similar_by_url(self.url)
Query(Story)

# Q 1864 : # Story.find_similar_by_url
Query(Story)

# Q 1865 : # self.url
Query(Story)
.select('url')
# Q 1866 : # Story.find_similar_by_url(self.url)
Query(Story)

# Q 1867 : # Story.find_similar_by_url
Query(Story)

# Q 1868 : # self.url
Query(Story)
.select('url')
# Q 1869 : # self.new_record?
Query(Story)

# Q 1870 : # Story.find_similar_by_url
Query(Story)

# Q 1871 : # self.url
Query(Story)
.select('url')
# Q 1872 : # @message.save
Query(Message)

# Q 1873 : # @message.save
Query(Message)

# Q 1874 : # @user.username
Query(User)
.select('username')
# Q 1875 : # @user.username
Query(User)
.select('username')
# Q 1876 : # @user.username
Query(User)
.select('username')
# Q 1877 : # @user.username
Query(User)
.select('username')
# Q 1878 : # @user.username
Query(User)
.select('username')
# Q 1879 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, s.id, c.id, u.id, Vote::COMMENT_REASONS.keys.first)
Query(Vote)

# Q 1880 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1881 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, s.id, c.id, u.id, Vote::COMMENT_REASONS.keys.first)
Query(Vote)

# Q 1882 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, s.id, c.id, u.id, Vote::COMMENT_REASONS.keys.first)
Query(Vote)

# Q 1883 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1884 : # stories.order("stories.created_at DESC")
Query(Story)
.order('id')
.order('created_at')
# Q 1885 : # stories.order
Query(Story)

# Q 1886 : # stories.order
Query(Story)

# Q 1887 : # hat.to_html_label
Query(Hat)

# Q 1888 : # hat.to_html_label
Query(Hat)

# Q 1889 : # self.where(:user_id => user_id, :comment_id => comment_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
# Q 1890 : # self.where(:user_id => user_id, :comment_id => comment_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
# Q 1891 : # Story.make!(:url => "http://flub.example.com")
Query(Story)

# Q 1892 : # Story.make!
Query(Story)

# Q 1893 : # Story.make!(:url => "http://flub.example.com")
Query(Story)

# Q 1894 : # Story.make!
Query(Story)

# Q 1895 : # Story.make!(:url => "http://flub.example.com")
Query(Story)

# Q 1896 : # Story.make!
Query(Story)

# Q 1897 : # Story.make!
Query(Story)

# Q 1898 : # Story.select(:id).where("`url` REGEXP '//([^/]*\.)?" + ActiveRecord::Base.connection.quote_string(domain) + "/'").collect(&:id)
Query(Story)
.select('id')
# Q 1899 : # Story.select(:id).where("`url` REGEXP '//([^/]*\.)?" + ActiveRecord::Base.connection.quote_string(domain) + "/'").collect(&:id)
Query(Story)
.select('id')
# Q 1900 : # Story.select(:id).where("`url` REGEXP '//([^/]*\.)?" + ActiveRecord::Base.connection.quote_string(domain) + "/'").collect
Query(Story)
.select('id')
# Q 1901 : # Story.select(:id).where("`url` REGEXP '//([^/]*\.)?" + ActiveRecord::Base.connection.quote_string(domain) + "/'")
Query(Story)
.select('id')
# Q 1902 : # Story.select(:id).where
Query(Story)
.select('id')
# Q 1903 : # Story.select(:id)
Query(Story)
.select('id')
# Q 1904 : # Story.select
Query(Story)

# Q 1905 : # Story.select(:id).where("`url` REGEXP '//([^/]*\.)?" + ActiveRecord::Base.connection.quote_string(domain) + "/'").collect
Query(Story)
.select('id')
# Q 1906 : # Story.select(:id).where
Query(Story)
.select('id')
# Q 1907 : # Story.select
Query(Story)

# Q 1908 : # Tag.all_with_filtered_counts_for(@user).map
Query(Tag)

# Q 1909 : # Tag.all_with_filtered_counts_for
Query(Tag)

# Q 1910 : # Story.new
Query(Story)

# Q 1911 : # Story.new
Query(Story)

# Q 1912 : # Story.new
Query(Story)

# Q 1913 : # comment.is_gone?
Query(Comment)

# Q 1914 : # comment.is_undeletable_by_user?
Query(Comment)

# Q 1915 : # if story.user_is_author?
#   
#   
# else
#   
#   
# end
Query(Story)

# Q 1916 : # story.user_is_author?
Query(Story)

# Q 1917 : # User.where(:username => username).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1918 : # User.where(:username => username).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1919 : # User.where(:username => username)
Query(User)
.where("username = ?")
# Q 1920 : # User.where(:username => username).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1921 : # User.validators_on(:username).select { |v|
#   
#   v.class == ActiveModel::Validations::FormatValidator
# }.first.options
Query(User)
.return_limit('1')
# Q 1922 : # User.validators_on(:username).select { |v|
#   
#   v.class == ActiveModel::Validations::FormatValidator
# }.first
Query(User)
.return_limit('1')
# Q 1923 : # User.validators_on(:username).select
Query(User)

# Q 1924 : # User.validators_on(:username)
Query(User)

# Q 1925 : # User.validators_on
Query(User)

# Q 1926 : # User.validators_on(:username).select { |v|
#   
#   v.class == ActiveModel::Validations::FormatValidator
# }.first.options
Query(User)
.return_limit('1')
# Q 1927 : # User.validators_on(:username).select { |v|
#   
#   v.class == ActiveModel::Validations::FormatValidator
# }.first
Query(User)
.return_limit('1')
# Q 1928 : # User.validators_on(:username).select
Query(User)

# Q 1929 : # User.validators_on
Query(User)

# Q 1930 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 1931 : # @user.id
Query(User)

# Q 1932 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 1933 : # @user.id
Query(User)

# Q 1934 : # @user.is_moderator?
Query(User)

# Q 1935 : # @user.is_moderator?
Query(User)

# Q 1936 : # votes.inject({ })
Query(Vote)

# Q 1937 : # votes.inject
Query(Vote)

# Q 1938 : # votes.inject
Query(Vote)

# Q 1939 : # Story.arel_table
Query(Story)

# Q 1940 : # Story.arel_table
Query(Story)

# Q 1941 : # Tagging.arel_table
Query(Tagging)

# Q 1942 : # Tagging.arel_table
Query(Tagging)

# Q 1943 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 1944 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 1945 : # InvitationRequest.where(:code => params[:code].to_s)
Query(InvitationRequest)
.where("code = ?")
# Q 1946 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 1947 : # Story.make!(:title => "Hello there, this is a title")
Query(Story)

# Q 1948 : # Story.make!
Query(Story)

# Q 1949 : # Story.make!(:title => "Hello there, this is a title")
Query(Story)

# Q 1950 : # Story.make!
Query(Story)

# Q 1951 : # Story.make!(:title => "Hello there, this is a title")
Query(Story)

# Q 1952 : # Story.make!
Query(Story)

# Q 1953 : # Story.make!
Query(Story)

# Q 1954 : # comment.is_gone?
Query(Comment)

# Q 1955 : # comment.is_deletable_by_user?
Query(Comment)

# Q 1956 : # Tagging.arel_table
Query(Tagging)

# Q 1957 : # tag.id
Query(Tag)

# Q 1958 : # Tagging.arel_table
Query(Tagging)

# Q 1959 : # tag.id
Query(Tag)

# Q 1960 : # comment.as_json
Query(Comment)

# Q 1961 : # comment.as_json
Query(Comment)

# Q 1962 : # self.increment_value_for(key, amount)
Query(Keystore)

# Q 1963 : # self.increment_value_for
Query(Keystore)

# Q 1964 : # self.increment_value_for
Query(Keystore)

# Q 1965 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 1966 : # @user.id
Query(User)

# Q 1967 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 1968 : # @user.id
Query(User)

# Q 1969 : # @user.is_moderator?
Query(User)

# Q 1970 : # @user.id
Query(User)

# Q 1971 : # comment.user_id
Query(Comment)
.select('user_id')
# Q 1972 : # self.description.to_s.strip
Query(Story)
.select('description')
# Q 1973 : # self.description.to_s
Query(Story)
.select('description')
# Q 1974 : # self.description
Query(Story)
.select('description')
# Q 1975 : # Tagging.arel_table
Query(Tagging)

# Q 1976 : # Tagging.arel_table
Query(Tagging)

# Q 1977 : # @story.fetched_attributes
Query(Story)

# Q 1978 : # @story.fetched_attributes
Query(Story)

# Q 1979 : # @story.fetched_attributes
Query(Story)

# Q 1980 : # Story.make!(:title => "Hello _ underscore")
Query(Story)

# Q 1981 : # Story.make!
Query(Story)

# Q 1982 : # Story.make!(:title => "Hello _ underscore")
Query(Story)

# Q 1983 : # Story.make!
Query(Story)

# Q 1984 : # Story.make!(:title => "Hello _ underscore")
Query(Story)

# Q 1985 : # Story.make!
Query(Story)

# Q 1986 : # Story.make!
Query(Story)

# Q 1987 : # Story.make!
Query(Story)

# Q 1988 : # s = Story.make!
Query(Story)

# Q 1989 : # s = Story.make!
Query(Story)

# Q 1990 : # Story.make!
Query(Story)

# Q 1991 : # stories.newest
Query(Story)

# Q 1992 : # stories.newest
Query(Story)

# Q 1993 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1994 : # Comment.make!
Query(Comment)

# Q 1995 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1996 : # Comment.make!
Query(Comment)

# Q 1997 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1998 : # Comment.make!
Query(Comment)

# Q 1999 : # Comment.make!
Query(Comment)

# Q 2000 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 2001 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 2002 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s)
Query(User)
.where(" = ?")
# Q 2003 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 2004 : # @story.url
Query(Story)
.select('url')
# Q 2005 : # @story.url
Query(Story)
.select('url')
# Q 2006 : # Invitation.new
Query(Invitation)

# Q 2007 : # Invitation.new
Query(Invitation)

# Q 2008 : # Invitation.new
Query(Invitation)

# Q 2009 : # self.incremented_value_for(key, amount)
Query(Keystore)

# Q 2010 : # self.incremented_value_for
Query(Keystore)

# Q 2011 : # self.incremented_value_for
Query(Keystore)

# Q 2012 : # @user.id
Query(User)

# Q 2013 : # @user.id
Query(User)

# Q 2014 : # @user.id
Query(User)

# Q 2015 : # @message.save!
Query(Message)

# Q 2016 : # @message.save!
Query(Message)

# Q 2017 : # comment.url
Query(Comment)

# Q 2018 : # comment.url
Query(Comment)

# Q 2019 : # Story.make!(:title => "Hello, underscore")
Query(Story)

# Q 2020 : # Story.make!
Query(Story)

# Q 2021 : # Story.make!(:title => "Hello, underscore")
Query(Story)

# Q 2022 : # Story.make!
Query(Story)

# Q 2023 : # Story.make!(:title => "Hello, underscore")
Query(Story)

# Q 2024 : # Story.make!
Query(Story)

# Q 2025 : # Story.make!
Query(Story)

# Q 2026 : # User.make!
Query(User)

# Q 2027 : # u = User.make!
Query(User)

# Q 2028 : # u = User.make!
Query(User)

# Q 2029 : # User.make!
Query(User)

# Q 2030 : # self.body
Query(Message)
.select('body')
# Q 2031 : # self.body
Query(Message)
.select('body')
# Q 2032 : # self.url.blank?
Query(Story)
.select('url')
# Q 2033 : # self.url
Query(Story)
.select('url')
# Q 2034 : # self.url.blank?
Query(Story)
.select('url')
# Q 2035 : # self.url
Query(Story)
.select('url')
# Q 2036 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id).first_or_initialize
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2037 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id).first_or_initialize
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2038 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2039 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id).first_or_initialize
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2040 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2041 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2042 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2043 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2044 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2045 : # Story.make(:title => "The One-second War (What Time Will You Die?) ")
Query(Story)

# Q 2046 : # Story.make
Query(Story)

# Q 2047 : # Story.make(:title => "The One-second War (What Time Will You Die?) ")
Query(Story)

# Q 2048 : # Story.make
Query(Story)

# Q 2049 : # Story.make(:title => "The One-second War (What Time Will You Die?) ")
Query(Story)

# Q 2050 : # Story.make
Query(Story)

# Q 2051 : # Story.make
Query(Story)

# Q 2052 : # comment.story.is_gone?
Query(Story)
.where("id = ?")
# Q 2053 : # comment.story
Query(Story)
.where("id = ?")
# Q 2054 : # comment.is_gone?
Query(Comment)

# Q 2055 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2056 : # @user.id
Query(User)

# Q 2057 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2058 : # @user.id
Query(User)

# Q 2059 : # @user.unread_message_count
Query(User)

# Q 2060 : # self.is_admin?
Query(User)

# Q 2061 : # self.is_admin?
Query(User)

# Q 2062 : # Story.find_similar_by_url(@story.url)
Query(Story)

# Q 2063 : # Story.find_similar_by_url(@story.url)
Query(Story)

# Q 2064 : # Story.find_similar_by_url
Query(Story)

# Q 2065 : # @story.url
Query(Story)
.select('url')
# Q 2066 : # Story.find_similar_by_url
Query(Story)

# Q 2067 : # @story.url
Query(Story)
.select('url')
# Q 2068 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2069 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2070 : # self.body.to_s
Query(Message)
.select('body')
# Q 2071 : # self.body
Query(Message)
.select('body')
# Q 2072 : # self.body.to_s
Query(Message)
.select('body')
# Q 2073 : # self.body
Query(Message)
.select('body')
# Q 2074 : # @user.show_story_previews?
Query(User)

# Q 2075 : # Story.score_sql
Query(Story)

# Q 2076 : # Story.score_sql
Query(Story)

# Q 2077 : # comment.is_editable_by_user?(@user)
Query(Comment)

# Q 2078 : # comment.is_editable_by_user?
Query(Comment)

# Q 2079 : # comment.is_editable_by_user?
Query(Comment)

# Q 2080 : # story.description_or_story_cache
Query(Story)

# Q 2081 : # User.make!
Query(User)

# Q 2082 : # u = User.make!
Query(User)

# Q 2083 : # u = User.make!
Query(User)

# Q 2084 : # User.make!
Query(User)

# Q 2085 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2086 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2087 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2088 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2089 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2090 : # comment.downvotes
Query(Comment)
.select('downvotes')
# Q 2091 : # self.short_id
Query(Message)
.select('short_id')
# Q 2092 : # self.short_id
Query(Message)
.select('short_id')
# Q 2093 : # Story.make!(:user_id => u.id)
Query(Story)

# Q 2094 : # Story.make!
Query(Story)

# Q 2095 : # Story.make!(:user_id => u.id)
Query(Story)

# Q 2096 : # Story.make!
Query(Story)

# Q 2097 : # Story.make!(:user_id => u.id)
Query(Story)

# Q 2098 : # Story.make!
Query(Story)

# Q 2099 : # Story.make!
Query(Story)

# Q 2100 : # comment.score
Query(Comment)

# Q 2101 : # comment.user_id
Query(Comment)
.select('user_id')
# Q 2102 : # @user.try
Query(User)

# Q 2103 : # @user.username
Query(User)
.select('username')
# Q 2104 : # @user.username
Query(User)
.select('username')
# Q 2105 : # @user.username
Query(User)
.select('username')
# Q 2106 : # @user.username
Query(User)
.select('username')
# Q 2107 : # @user.username
Query(User)
.select('username')
# Q 2108 : # @user.try
Query(User)

# Q 2109 : # Vote.transaction
Query(Vote)

# Q 2110 : # Vote.transaction
Query(Vote)

# Q 2111 : # Story.unmerged.where(is_expired: false)
Query(Story)
.where("is_expired = ?")
# Q 2112 : # Story.unmerged.where
Query(Story)

# Q 2113 : # Story.unmerged
Query(Story)

# Q 2114 : # Story.unmerged.where
Query(Story)

# Q 2115 : # Story.unmerged
Query(Story)

# Q 2116 : # Tag.where(:tag => cookies[TAG_FILTER_COOKIE].to_s.split(","))
Query(Tag)
.where("tag = ?")
# Q 2117 : # comment.vote_summary_for_user(@user).downcase
Query(Comment)

# Q 2118 : # comment.vote_summary_for_user
Query(Comment)

# Q 2119 : # @user.is_moderator?
Query(User)

# Q 2120 : # @user.is_moderator?
Query(User)

# Q 2121 : # User.make!
Query(User)

# Q 2122 : # u = User.make!
Query(User)

# Q 2123 : # u = User.make!
Query(User)

# Q 2124 : # User.make!
Query(User)

# Q 2125 : # comment.current_vote
Query(Comment)

# Q 2126 : # comment.current_vote
Query(Comment)

# Q 2127 : # @user.username
Query(User)
.select('username')
# Q 2128 : # comment.current_vote
Query(Comment)

# Q 2129 : # @user.karma
Query(User)
.select('karma')
# Q 2130 : # @user.show_avatars?
Query(User)

# Q 2131 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2132 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2133 : # Message.where(:short_id => m[1])
Query(Message)
.where("short_id = ?")
# Q 2134 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2135 : # Message.where(:short_id => m[1])
Query(Message)
.where("short_id = ?")
# Q 2136 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2137 : # Message.where(:short_id => m[1])
Query(Message)
.where("short_id = ?")
# Q 2138 : # message = Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2139 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2140 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2141 : # story.user
Query(User)
.where("id = ?")
# Q 2142 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2143 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2144 : # InvitationRequest.where(:code => params[:code].to_s)
Query(InvitationRequest)
.where("code = ?")
# Q 2145 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2146 : # story.user.avatar_url
Query(User)
.where("id = ?")
# Q 2147 : # story.user
Query(User)
.where("id = ?")
# Q 2148 : # Comment.all.each
Query(Comment)

# Q 2149 : # Comment.all
Query(Comment)

# Q 2150 : # Comment.all.each
Query(Comment)

# Q 2151 : # Comment.all
Query(Comment)

# Q 2152 : # self.email.strip.downcase
Query(User)
.select('email')
# Q 2153 : # self.email.strip
Query(User)
.select('email')
# Q 2154 : # self.email
Query(User)
.select('email')
# Q 2155 : # self.email.strip.downcase
Query(User)
.select('email')
# Q 2156 : # self.email.strip
Query(User)
.select('email')
# Q 2157 : # self.email
Query(User)
.select('email')
# Q 2158 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2159 : # @user.id
Query(User)

# Q 2160 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2161 : # @user.id
Query(User)

# Q 2162 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2163 : # @user.id
Query(User)

# Q 2164 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2165 : # @user.id
Query(User)

# Q 2166 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2167 : # @user.id
Query(User)

# Q 2168 : # Story.make
Query(Story)

# Q 2169 : # s = Story.make
Query(Story)

# Q 2170 : # s = Story.make
Query(Story)

# Q 2171 : # Story.make
Query(Story)

# Q 2172 : # tag.tag
Query(Tag)
.select('tag')
# Q 2173 : # story.user.avatar_url
Query(User)
.where("id = ?")
# Q 2174 : # story.user
Query(User)
.where("id = ?")
# Q 2175 : # User.where(:password_reset_token => params[:token].to_s).first
Query(User)
.where("password_reset_token = ?")
.return_limit('1')
# Q 2176 : # User.where(:password_reset_token => params[:token].to_s).first
Query(User)
.where("password_reset_token = ?")
.return_limit('1')
# Q 2177 : # User.where(:password_reset_token => params[:token].to_s)
Query(User)
.where("password_reset_token = ?")
# Q 2178 : # User.where(:password_reset_token => params[:token].to_s).first
Query(User)
.where("password_reset_token = ?")
.return_limit('1')
# Q 2179 : # @story.title.present?
Query(Story)
.select('title')
# Q 2180 : # @story.title
Query(Story)
.select('title')
# Q 2181 : # @story.title.present?
Query(Story)
.select('title')
# Q 2182 : # @story.title
Query(Story)
.select('title')
# Q 2183 : # tag.css_class
Query(Tag)

# Q 2184 : # tag.description
Query(Tag)
.select('description')
# Q 2185 : # story.user.avatar_url
Query(User)
.where("id = ?")
# Q 2186 : # story.user
Query(User)
.where("id = ?")
# Q 2187 : # Comment.new
Query(Comment)

# Q 2188 : # Comment.new
Query(Comment)

# Q 2189 : # Comment.new
Query(Comment)

# Q 2190 : # tag.tag
Query(Tag)
.select('tag')
# Q 2191 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2192 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2193 : # User.where(:username => params[:user])
Query(User)
.where("username = ?")
# Q 2194 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2195 : # story.previewing
Query(Story)

# Q 2196 : # self.results.total_entries
Query(Search)

# Q 2197 : # self.results.total_entries
Query(Search)

# Q 2198 : # self.results
Query(Search)

# Q 2199 : # self.results.total_entries
Query(Search)

# Q 2200 : # self.results
Query(Search)

# Q 2201 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2202 : # @user.id
Query(User)

# Q 2203 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2204 : # @user.id
Query(User)

# Q 2205 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2206 : # @user.id
Query(User)

# Q 2207 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2208 : # @user.id
Query(User)

# Q 2209 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2210 : # @user.id
Query(User)

# Q 2211 : # comment.story.comments_path
Query(Story)
.where("id = ?")
# Q 2212 : # comment.story
Query(Story)
.where("id = ?")
# Q 2213 : # comment.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 2214 : # comment.story
Query(Story)
.where("id = ?")
# Q 2215 : # story.user_is_author?
Query(Story)

# Q 2216 : # self.karma
Query(User)
.select('karma')
# Q 2217 : # self.karma
Query(User)
.select('karma')
# Q 2218 : # self.karma
Query(User)
.select('karma')
# Q 2219 : # Story.make
Query(Story)

# Q 2220 : # s = Story.make
Query(Story)

# Q 2221 : # s = Story.make
Query(Story)

# Q 2222 : # Story.make
Query(Story)

# Q 2223 : # stories.newest_by_user(by_user)
Query(Story)

# Q 2224 : # stories.newest_by_user
Query(Story)

# Q 2225 : # stories.newest_by_user
Query(Story)

# Q 2226 : # self.stories_submitted_count
Query(User)

# Q 2227 : # self.comments_posted_count
Query(User)

# Q 2228 : # self.stories_submitted_count
Query(User)

# Q 2229 : # self.comments_posted_count
Query(User)

# Q 2230 : # Story.arel_table
Query(Story)

# Q 2231 : # Story.arel_table
Query(Story)

# Q 2232 : # Story.new(story_params)
Query(Story)

# Q 2233 : # Story.new(story_params)
Query(Story)

# Q 2234 : # Story.new
Query(Story)

# Q 2235 : # Story.new
Query(Story)

# Q 2236 : # self.page
Query(Search)

# Q 2237 : # self.page_count
Query(Search)

# Q 2238 : # self.page
Query(Search)

# Q 2239 : # self.page_count
Query(Search)

# Q 2240 : # @user.id
Query(User)

# Q 2241 : # @user.id
Query(User)

# Q 2242 : # @user.id
Query(User)

# Q 2243 : # comment.is_gone?
Query(Comment)

# Q 2244 : # story.html_class_for_user
Query(Story)

# Q 2245 : # self.page_count
Query(Search)

# Q 2246 : # self.page_count
Query(Search)

# Q 2247 : # self.page_count
Query(Search)

# Q 2248 : # message.save!
Query(Message)

# Q 2249 : # message.save!
Query(Message)

# Q 2250 : # message.save!
Query(Message)

# Q 2251 : # message.save!
Query(Message)

# Q 2252 : # message.save!
Query(Message)

# Q 2253 : # message.save!
Query(Message)

# Q 2254 : # User.where(:rss_token => params[:token].to_s).first
Query(User)
.where("rss_token = ?")
.return_limit('1')
# Q 2255 : # User.where(:rss_token => params[:token].to_s).first
Query(User)
.where("rss_token = ?")
.return_limit('1')
# Q 2256 : # User.where(:rss_token => params[:token].to_s)
Query(User)
.where("rss_token = ?")
# Q 2257 : # User.where(:rss_token => params[:token].to_s).first
Query(User)
.where("rss_token = ?")
.return_limit('1')
# Q 2258 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2259 : # story.user
Query(User)
.where("id = ?")
# Q 2260 : # Story.votes_cast_type
Query(Story)

# Q 2261 : # Story.votes_cast_type
Query(Story)

# Q 2262 : # comment.is_deletable_by_user?(@user)
Query(Comment)

# Q 2263 : # comment.is_deletable_by_user?
Query(Comment)

# Q 2264 : # comment.is_deletable_by_user?
Query(Comment)

# Q 2265 : # Story.votes_cast_type
Query(Story)

# Q 2266 : # Story.votes_cast_type
Query(Story)

# Q 2267 : # Vote.new(:vote => 1)
Query(Vote)

# Q 2268 : # Vote.new(:vote => 1)
Query(Vote)

# Q 2269 : # Vote.new
Query(Vote)

# Q 2270 : # Vote.new
Query(Vote)

# Q 2271 : # Story.make(:title => "blah")
Query(Story)

# Q 2272 : # Story.make
Query(Story)

# Q 2273 : # Story.make(:title => "blah")
Query(Story)

# Q 2274 : # Story.make
Query(Story)

# Q 2275 : # Story.make(:title => "blah")
Query(Story)

# Q 2276 : # Story.make
Query(Story)

# Q 2277 : # Story.make
Query(Story)

# Q 2278 : # comment.gone_text
Query(Comment)

# Q 2279 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2280 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2281 : # story.user_is_author?
Query(Story)

# Q 2282 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2283 : # @user.id
Query(User)

# Q 2284 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2285 : # @user.id
Query(User)

# Q 2286 : # Story.where(:url => urls, :is_expired => false).order("id DESC").first
Query(Story)
.where("url = ?")
.where("is_expired = ?")
.order('id')
.order('id')
.return_limit('1')
# Q 2287 : # Story.where(:url => urls, :is_expired => false).order("id DESC").first
Query(Story)
.where("url = ?")
.where("is_expired = ?")
.order('id')
.order('id')
.return_limit('1')
# Q 2288 : # Story.where(:url => urls, :is_expired => false).order("id DESC")
Query(Story)
.where("url = ?")
.where("is_expired = ?")
.order('id')
.order('id')
# Q 2289 : # Story.where(:url => urls, :is_expired => false).order
Query(Story)
.where("url = ?")
.where("is_expired = ?")
# Q 2290 : # Story.where(:url => urls, :is_expired => false)
Query(Story)
.where("url = ?")
.where("is_expired = ?")
# Q 2291 : # Story.where(:url => urls, :is_expired => false).order("id DESC").first
Query(Story)
.where("url = ?")
.where("is_expired = ?")
.order('id')
.order('id')
.return_limit('1')
# Q 2292 : # Story.where(:url => urls, :is_expired => false).order
Query(Story)
.where("url = ?")
.where("is_expired = ?")
# Q 2293 : # @story.valid?
Query(Story)

# Q 2294 : # @story.valid?
Query(Story)

# Q 2295 : # comment.delete_for_user(@user, params[:reason])
Query(Comment)

# Q 2296 : # comment.delete_for_user
Query(Comment)

# Q 2297 : # comment.delete_for_user
Query(Comment)

# Q 2298 : # Vote.comment_votes_by_user_for_comment_ids_hash(user.id, self.results.select { |r|
#   
#   r.class == Comment
# }.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 2299 : # Vote.comment_votes_by_user_for_comment_ids_hash(user.id, self.results.select { |r|
#   
#   r.class == Comment
# }.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 2300 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2301 : # user.id
Query(User)

# Q 2302 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2303 : # user.id
Query(User)

# Q 2304 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2305 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2306 : # comment.markeddown_comment
Query(Comment)
.select('markeddown_comment')
# Q 2307 : # self.delete!
Query(User)

# Q 2308 : # self.delete!
Query(User)

# Q 2309 : # self.results.select { |r|
#   
#   r.class == Comment
# }.map
Query(Search)

# Q 2310 : # self.results.select
Query(Search)

# Q 2311 : # self.results
Query(Search)

# Q 2312 : # self.results.select { |r|
#   
#   r.class == Comment
# }.map
Query(Search)

# Q 2313 : # self.results.select
Query(Search)

# Q 2314 : # self.results
Query(Search)

# Q 2315 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2316 : # story.user
Query(User)
.where("id = ?")
# Q 2317 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2318 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2319 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2320 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2321 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2322 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2323 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2324 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2325 : # self.results.each
Query(Search)

# Q 2326 : # self.results
Query(Search)

# Q 2327 : # self.results.each
Query(Search)

# Q 2328 : # self.results
Query(Search)

# Q 2329 : # @user.update_unread_message_count!
Query(User)

# Q 2330 : # @user.update_unread_message_count!
Query(User)

# Q 2331 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"])
Query(Story)

# Q 2332 : # Story.make!
Query(Story)

# Q 2333 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"])
Query(Story)

# Q 2334 : # Story.make!
Query(Story)

# Q 2335 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"])
Query(Story)

# Q 2336 : # Story.make!
Query(Story)

# Q 2337 : # Story.make!
Query(Story)

# Q 2338 : # story.html_class_for_user
Query(Story)

# Q 2339 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2340 : # story.user
Query(User)
.where("id = ?")
# Q 2341 : # Moderation.new
Query(Moderation)

# Q 2342 : # Moderation.new
Query(Moderation)

# Q 2343 : # Moderation.new
Query(Moderation)

# Q 2344 : # story.created_at
Query(Story)
.select('created_at')
# Q 2345 : # Story.score_sql
Query(Story)

# Q 2346 : # Story.score_sql
Query(Story)

# Q 2347 : # comment.is_undeletable_by_user?(@user)
Query(Comment)

# Q 2348 : # comment.is_undeletable_by_user?
Query(Comment)

# Q 2349 : # comment.is_undeletable_by_user?
Query(Comment)

# Q 2350 : # @user.is_new?
Query(User)

# Q 2351 : # self.id
Query(User)

# Q 2352 : # self.id
Query(User)

# Q 2353 : # self.id
Query(User)

# Q 2354 : # Story.all.order("id DESC").each
Query(Story)
.order('id')
.order('id')
# Q 2355 : # Story.all.order("id DESC")
Query(Story)
.order('id')
.order('id')
# Q 2356 : # Story.all.order
Query(Story)

# Q 2357 : # Story.all
Query(Story)

# Q 2358 : # Story.all.order("id DESC").each
Query(Story)
.order('id')
.order('id')
# Q 2359 : # Story.all.order
Query(Story)

# Q 2360 : # Story.all
Query(Story)

# Q 2361 : # Story.where(:short_id => params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 2362 : # Story.where(:short_id => params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 2363 : # Story.where(:short_id => params[:id])
Query(Story)
.where("short_id = ?")
# Q 2364 : # Story.where(:short_id => params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 2365 : # InvitationRequest.verified_count
Query(InvitationRequest)

# Q 2366 : # story.is_editable_by_user?
Query(Story)

# Q 2367 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2368 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2369 : # story.short_id
Query(Story)
.select('short_id')
# Q 2370 : # self.is_gone?
Query(Comment)

# Q 2371 : # self.gone_text
Query(Comment)

# Q 2372 : # self.is_gone?
Query(Comment)

# Q 2373 : # self.gone_text
Query(Comment)

# Q 2374 : # @story.title
Query(Story)
.select('title')
# Q 2375 : # @story.title
Query(Story)
.select('title')
# Q 2376 : # @message.save
Query(Message)

# Q 2377 : # @message.save
Query(Message)

# Q 2378 : # comment.undelete_for_user(@user)
Query(Comment)

# Q 2379 : # comment.undelete_for_user
Query(Comment)

# Q 2380 : # comment.undelete_for_user
Query(Comment)

# Q 2381 : # User.make!(:username => "mod", :is_moderator => true)
Query(User)

# Q 2382 : # User.make!
Query(User)

# Q 2383 : # User.make!(:username => "mod", :is_moderator => true)
Query(User)

# Q 2384 : # User.make!
Query(User)

# Q 2385 : # User.make!(:username => "mod", :is_moderator => true)
Query(User)

# Q 2386 : # User.make!
Query(User)

# Q 2387 : # User.make!
Query(User)

# Q 2388 : # @user.is_moderator?
Query(User)

# Q 2389 : # @user.is_admin?
Query(User)

# Q 2390 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2391 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2392 : # Story.find
Query(Story)
.where("id = ?")
# Q 2393 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2394 : # Story.find
Query(Story)
.where("id = ?")
# Q 2395 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2396 : # Story.find
Query(Story)
.where("id = ?")
# Q 2397 : # Story.find
Query(Story)
.where("id = ?")
# Q 2398 : # Vote.story_votes_by_user_for_story_ids_hash(user.id, self.results.select { |r|
#   
#   r.class == Story
# }.map { |s|
#   
#   s.id
# })
Query(Vote)

# Q 2399 : # Vote.story_votes_by_user_for_story_ids_hash(user.id, self.results.select { |r|
#   
#   r.class == Story
# }.map { |s|
#   
#   s.id
# })
Query(Vote)

# Q 2400 : # Vote.story_votes_by_user_for_story_ids_hash
Query(Vote)

# Q 2401 : # user.id
Query(User)

# Q 2402 : # Vote.story_votes_by_user_for_story_ids_hash
Query(Vote)

# Q 2403 : # user.id
Query(User)

# Q 2404 : # Story.arel_table
Query(Story)

# Q 2405 : # Story.arel_table
Query(Story)

# Q 2406 : # @story.merged_into_story.comments_path
Query(Story)
.where("id = ?")
# Q 2407 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2408 : # @story.merged_into_story.comments_path
Query(Story)
.where("id = ?")
# Q 2409 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2410 : # stories.recent
Query(Story)

# Q 2411 : # stories.recent
Query(Story)

# Q 2412 : # HatRequest.count
Query(HatRequest)

# Q 2413 : # story.is_gone?
Query(Story)

# Q 2414 : # story.is_undeletable_by_user?
Query(Story)

# Q 2415 : # self.results.select { |r|
#   
#   r.class == Story
# }.map
Query(Search)

# Q 2416 : # self.results.select
Query(Search)

# Q 2417 : # self.results
Query(Search)

# Q 2418 : # self.results.select { |r|
#   
#   r.class == Story
# }.map
Query(Search)

# Q 2419 : # self.results.select
Query(Search)

# Q 2420 : # self.results
Query(Search)

# Q 2421 : # Tagging.arel_table
Query(Tagging)

# Q 2422 : # Tagging.arel_table
Query(Tagging)

# Q 2423 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"], :description => "desc")
Query(Story)

# Q 2424 : # Story.make!
Query(Story)

# Q 2425 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"], :description => "desc")
Query(Story)

# Q 2426 : # Story.make!
Query(Story)

# Q 2427 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"], :description => "desc")
Query(Story)

# Q 2428 : # Story.make!
Query(Story)

# Q 2429 : # Story.make!
Query(Story)

# Q 2430 : # Tagging.arel_table
Query(Tagging)

# Q 2431 : # Tagging.arel_table
Query(Tagging)

# Q 2432 : # stories.newest
Query(Story)

# Q 2433 : # stories.newest
Query(Story)

# Q 2434 : # story.short_id
Query(Story)
.select('short_id')
# Q 2435 : # self.results.each
Query(Search)

# Q 2436 : # self.results
Query(Search)

# Q 2437 : # self.results.each
Query(Search)

# Q 2438 : # self.results
Query(Search)

# Q 2439 : # @story.can_be_seen_by_user?(@user)
Query(Story)

# Q 2440 : # @story.can_be_seen_by_user?
Query(Story)

# Q 2441 : # @story.can_be_seen_by_user?
Query(Story)

# Q 2442 : # Tagging.arel_table
Query(Tagging)

# Q 2443 : # Tagging.arel_table
Query(Tagging)

# Q 2444 : # @story.title
Query(Story)
.select('title')
# Q 2445 : # @story.title
Query(Story)
.select('title')
# Q 2446 : # @story.title
Query(Story)
.select('title')
# Q 2447 : # story.is_gone?
Query(Story)

# Q 2448 : # comment.is_editable_by_user?(@user)
Query(Comment)

# Q 2449 : # comment.is_editable_by_user?
Query(Comment)

# Q 2450 : # comment.is_editable_by_user?
Query(Comment)

# Q 2451 : # story.user_id
Query(Story)
.select('user_id')
# Q 2452 : # @user.try
Query(User)

# Q 2453 : # Story.connection.adapter_name.match(/mysql/i)
Query(Story)

# Q 2454 : # Story.connection.adapter_name.match
Query(Story)

# Q 2455 : # Story.connection.adapter_name
Query(Story)

# Q 2456 : # Story.connection
Query(Story)

# Q 2457 : # Story.connection.adapter_name.match
Query(Story)

# Q 2458 : # Story.connection.adapter_name
Query(Story)

# Q 2459 : # Story.connection
Query(Story)

# Q 2460 : # @user.try
Query(User)

# Q 2461 : # self.send(k)
Query(Comment)

# Q 2462 : # self.send(k)
Query(Comment)

# Q 2463 : # self.send
Query(Comment)

# Q 2464 : # self.send(k)
Query(Comment)

# Q 2465 : # self.send
Query(Comment)

# Q 2466 : # self.send(k)
Query(Comment)

# Q 2467 : # self.send
Query(Comment)

# Q 2468 : # self.send
Query(Comment)

# Q 2469 : # @story.short_id_url
Query(Story)

# Q 2470 : # @story.short_id_url
Query(Story)

# Q 2471 : # @story.short_id_url
Query(Story)

# Q 2472 : # story.short_id
Query(Story)
.select('short_id')
# Q 2473 : # @story.merged_comments.includes(:user, :story, :hat).arrange_for_user(@user)
Query(Story)
.includes('user')
# Q 2474 : # @story.merged_comments.includes(:user, :story, :hat).arrange_for_user(@user)
Query(Story)
.includes('user')
# Q 2475 : # @story.merged_comments.includes(:user, :story, :hat).arrange_for_user
Query(Story)
.includes('user')
# Q 2476 : # @story.merged_comments.includes(:user, :story, :hat)
Query(Story)
.includes('user')
# Q 2477 : # @story.merged_comments.includes
Query(Story)

# Q 2478 : # @story.merged_comments
Query(Story)

# Q 2479 : # @story.merged_comments.includes(:user, :story, :hat).arrange_for_user
Query(Story)
.includes('user')
# Q 2480 : # @story.merged_comments.includes
Query(Story)

# Q 2481 : # @story.merged_comments
Query(Story)

# Q 2482 : # self.send(k.values.first)
Query(Comment)

# Q 2483 : # self.send(k.values.first)
Query(Comment)

# Q 2484 : # self.send
Query(Comment)

# Q 2485 : # self.send(k.values.first)
Query(Comment)

# Q 2486 : # self.send
Query(Comment)

# Q 2487 : # self.send(k.values.first)
Query(Comment)

# Q 2488 : # self.send
Query(Comment)

# Q 2489 : # self.send(k.values.first)
Query(Comment)

# Q 2490 : # self.send
Query(Comment)

# Q 2491 : # self.send
Query(Comment)

# Q 2492 : # Message.where(:short_id => params[:message_id] || params[:id]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2493 : # Message.where(:short_id => params[:message_id] || params[:id]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2494 : # Message.where(:short_id => params[:message_id] || params[:id])
Query(Message)
.where("short_id = ?")
# Q 2495 : # Message.where(:short_id => params[:message_id] || params[:id]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2496 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2497 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2498 : # @user.hats.where(:id => params[:hat_id])
Query(Hat)
.where("user_id = ?")
.where("id = ?")
# Q 2499 : # @user.hats.where
Query(Hat)
.where("user_id = ?")
# Q 2500 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 2501 : # @user.hats.where
Query(Hat)
.where("user_id = ?")
# Q 2502 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 2503 : # Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2504 : # mod_log = Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2505 : # mod_log = Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2506 : # Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2507 : # story.short_id
Query(Story)
.select('short_id')
# Q 2508 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2509 : # @user.id
Query(User)

# Q 2510 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2511 : # @user.id
Query(User)

# Q 2512 : # @comments.each
Query(Comment)

# Q 2513 : # @comments.each
Query(Comment)

# Q 2514 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2515 : # @user.id
Query(User)

# Q 2516 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2517 : # @user.id
Query(User)

# Q 2518 : # comment.save
Query(Comment)

# Q 2519 : # comment.save
Query(Comment)

# Q 2520 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, [comment.id])
Query(Vote)

# Q 2521 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, [comment.id])
Query(Vote)

# Q 2522 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2523 : # @user.id
Query(User)

# Q 2524 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2525 : # @user.id
Query(User)

# Q 2526 : # Tag.where(:tag => params[:tag]).first!
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 2527 : # Tag.where(:tag => params[:tag]).first!
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 2528 : # Tag.where(:tag => params[:tag])
Query(Tag)
.where("tag = ?")
# Q 2529 : # Tag.where(:tag => params[:tag]).first!
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 2530 : # comment.id
Query(Comment)

# Q 2531 : # comment.id
Query(Comment)

# Q 2532 : # story.can_have_suggestions_from_user?
Query(Story)

# Q 2533 : # comment.id
Query(Comment)

# Q 2534 : # comment.id
Query(Comment)

# Q 2535 : # story.short_id
Query(Story)
.select('short_id')
# Q 2536 : # stories.tagged(@tag)
Query(Story)

# Q 2537 : # stories.tagged
Query(Story)

# Q 2538 : # stories.tagged
Query(Story)

# Q 2539 : # story.is_gone?
Query(Story)

# Q 2540 : # self.calculated_confidence
Query(Comment)

# Q 2541 : # self.calculated_confidence
Query(Comment)

# Q 2542 : # self.calculated_confidence
Query(Comment)

# Q 2543 : # story.vote
Query(Story)

# Q 2544 : # story.vote
Query(Story)

# Q 2545 : # @tag.description.blank?
Query(Tag)
.select('description')
# Q 2546 : # @tag.description
Query(Tag)
.select('description')
# Q 2547 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2548 : # @tag.description
Query(Tag)
.select('description')
# Q 2549 : # @tag.description.blank?
Query(Tag)
.select('description')
# Q 2550 : # @tag.description
Query(Tag)
.select('description')
# Q 2551 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2552 : # @tag.description
Query(Tag)
.select('description')
# Q 2553 : # self.tags.map { |t|
#   
#   t.tag
# }.sort
Query(Tag)
.where("story_id = ?")
# Q 2554 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 2555 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 2556 : # self.tags.map { |t|
#   
#   t.tag
# }.sort
Query(Tag)
.where("story_id = ?")
# Q 2557 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 2558 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 2559 : # @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2560 : # @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2561 : # @story.comments
Query(Comment)
.where("story_id = ?")
# Q 2562 : # @comment = @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2563 : # @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2564 : # @story.comments
Query(Comment)
.where("story_id = ?")
# Q 2565 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2566 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2567 : # story.vote
Query(Story)

# Q 2568 : # @user.can_downvote?
Query(User)

# Q 2569 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2570 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2571 : # ShortId.new(self.class)
Query(ShortId)

# Q 2572 : # ShortId.new
Query(ShortId)

# Q 2573 : # self.class
Query(Comment)

# Q 2574 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2575 : # ShortId.new
Query(ShortId)

# Q 2576 : # self.class
Query(Comment)

# Q 2577 : # self.is_new?
Query(User)

# Q 2578 : # self.karma
Query(User)
.select('karma')
# Q 2579 : # self.is_new?
Query(User)

# Q 2580 : # self.karma
Query(User)
.select('karma')
# Q 2581 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2582 : # @tag.description
Query(Tag)
.select('description')
# Q 2583 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2584 : # @tag.description
Query(Tag)
.select('description')
# Q 2585 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2586 : # @tag.tag
Query(Tag)
.select('tag')
# Q 2587 : # story.is_hidden_by_cur_user
Query(Story)

# Q 2588 : # @story.title
Query(Story)
.select('title')
# Q 2589 : # @story.title
Query(Story)
.select('title')
# Q 2590 : # @story.title
Query(Story)
.select('title')
# Q 2591 : # story.short_id
Query(Story)
.select('short_id')
# Q 2592 : # self.session_token.blank?
Query(User)
.select('session_token')
# Q 2593 : # self.session_token
Query(User)
.select('session_token')
# Q 2594 : # self.session_token.blank?
Query(User)
.select('session_token')
# Q 2595 : # self.session_token
Query(User)
.select('session_token')
# Q 2596 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2597 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2598 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2599 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2600 : # self.parent_comment_id.present?
Query(Comment)
.select('parent_comment_id')
# Q 2601 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 2602 : # self.parent_comment_id.present?
Query(Comment)
.select('parent_comment_id')
# Q 2603 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 2604 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2605 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2606 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2607 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2608 : # self.parent_comment.thread_id
Query(Comment)
.where("id = ?")
.select('thread_id')
# Q 2609 : # self.parent_comment.thread_id
Query(Comment)
.where("id = ?")
.select('thread_id')
# Q 2610 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 2611 : # self.parent_comment.thread_id
Query(Comment)
.where("id = ?")
.select('thread_id')
# Q 2612 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 2613 : # story.short_id
Query(Story)
.select('short_id')
# Q 2614 : # Keystore.incremented_value_for("thread_id")
Query(Keystore)

# Q 2615 : # Keystore.incremented_value_for("thread_id")
Query(Keystore)

# Q 2616 : # Keystore.incremented_value_for
Query(Keystore)

# Q 2617 : # Keystore.incremented_value_for
Query(Keystore)

# Q 2618 : # self.send(k)
Query(Story)

# Q 2619 : # self.send(k)
Query(Story)

# Q 2620 : # self.send
Query(Story)

# Q 2621 : # self.send(k)
Query(Story)

# Q 2622 : # self.send
Query(Story)

# Q 2623 : # self.send(k)
Query(Story)

# Q 2624 : # self.send
Query(Story)

# Q 2625 : # self.send
Query(Story)

# Q 2626 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, comment.story_id, comment.id, @user.id, nil)
Query(Vote)

# Q 2627 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2628 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2629 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2630 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2631 : # comment.id
Query(Comment)

# Q 2632 : # @user.id
Query(User)

# Q 2633 : # comment.id
Query(Comment)

# Q 2634 : # @user.id
Query(User)

# Q 2635 : # story.hider_count
Query(Story)

# Q 2636 : # self.mailing_list_token.blank?
Query(User)
.select('mailing_list_token')
# Q 2637 : # self.mailing_list_token
Query(User)
.select('mailing_list_token')
# Q 2638 : # self.mailing_list_token.blank?
Query(User)
.select('mailing_list_token')
# Q 2639 : # self.mailing_list_token
Query(User)
.select('mailing_list_token')
# Q 2640 : # story.hider_count
Query(Story)

# Q 2641 : # self.send(k.values.first)
Query(Story)

# Q 2642 : # self.send(k.values.first)
Query(Story)

# Q 2643 : # self.send
Query(Story)

# Q 2644 : # self.send(k.values.first)
Query(Story)

# Q 2645 : # self.send
Query(Story)

# Q 2646 : # self.send(k.values.first)
Query(Story)

# Q 2647 : # self.send
Query(Story)

# Q 2648 : # self.send(k.values.first)
Query(Story)

# Q 2649 : # self.send
Query(Story)

# Q 2650 : # self.send
Query(Story)

# Q 2651 : # story.url.present?
Query(Story)
.select('url')
# Q 2652 : # story.url
Query(Story)
.select('url')
# Q 2653 : # @story.as_json(:with_comments => @comments)
Query(Story)

# Q 2654 : # @story.as_json
Query(Story)

# Q 2655 : # @story.as_json(:with_comments => @comments)
Query(Story)

# Q 2656 : # @story.as_json
Query(Story)

# Q 2657 : # @story.as_json
Query(Story)

# Q 2658 : # story.url
Query(Story)
.select('url')
# Q 2659 : # self.rss_token.blank?
Query(User)
.select('rss_token')
# Q 2660 : # self.rss_token
Query(User)
.select('rss_token')
# Q 2661 : # self.rss_token.blank?
Query(User)
.select('rss_token')
# Q 2662 : # self.rss_token
Query(User)
.select('rss_token')
# Q 2663 : # @user.id
Query(User)

# Q 2664 : # story.is_gone?
Query(Story)

# Q 2665 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, comment.story_id, comment.id, @user.id, params[:reason])
Query(Vote)

# Q 2666 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2667 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2668 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2669 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2670 : # comment.id
Query(Comment)

# Q 2671 : # @user.id
Query(User)

# Q 2672 : # comment.id
Query(Comment)

# Q 2673 : # @user.id
Query(User)

# Q 2674 : # @story.can_have_suggestions_from_user?(@user)
Query(Story)

# Q 2675 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 2676 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 2677 : # story.comments_path
Query(Story)

# Q 2678 : # Keystore.value_for
Query(Keystore)

# Q 2679 : # self.id
Query(User)

# Q 2680 : # Keystore.value_for
Query(Keystore)

# Q 2681 : # self.id
Query(User)

# Q 2682 : # self.calculated_hotness
Query(Story)

# Q 2683 : # self.calculated_hotness
Query(Story)

# Q 2684 : # self.calculated_hotness
Query(Story)

# Q 2685 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2686 : # @story.comments_path
Query(Story)

# Q 2687 : # @story.comments_path
Query(Story)

# Q 2688 : # stories.top(length)
Query(Story)

# Q 2689 : # stories.top
Query(Story)

# Q 2690 : # stories.top
Query(Story)

# Q 2691 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2692 : # User.transaction
Query(User)

# Q 2693 : # User.transaction
Query(User)

# Q 2694 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2695 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2696 : # ShortId.new(self.class)
Query(ShortId)

# Q 2697 : # ShortId.new
Query(ShortId)

# Q 2698 : # self.class
Query(Story)

# Q 2699 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2700 : # ShortId.new
Query(ShortId)

# Q 2701 : # self.class
Query(Story)

# Q 2702 : # @story.suggested_taggings.where(:user_id => @user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 2703 : # @story.suggested_taggings.where(:user_id => @user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 2704 : # @story.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2705 : # @story.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2706 : # @user.id
Query(User)

# Q 2707 : # @story.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2708 : # @story.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2709 : # @user.id
Query(User)

# Q 2710 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2711 : # self.comments.each
Query(Comment)
.where("user_id = ?")
# Q 2712 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 2713 : # self.comments.each { |c|
#   
#   c.delete_for_user(self)
# }
Query(Comment)
.where("user_id = ?")
# Q 2714 : # self.comments.each
Query(Comment)
.where("user_id = ?")
# Q 2715 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 2716 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 2717 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 2718 : # self.sent_messages.each do |m|
#   
#   m.deleted_by_author = true
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 2719 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 2720 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 2721 : # @story.suggested_titles.where(:user_id => @user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 2722 : # @story.suggested_titles.where(:user_id => @user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 2723 : # @story.suggested_titles.where(:user_id => @user.id)
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
# Q 2724 : # @story.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 2725 : # @story.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 2726 : # @user.id
Query(User)

# Q 2727 : # @story.suggested_titles.where(:user_id => @user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 2728 : # @story.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 2729 : # @story.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 2730 : # @user.id
Query(User)

# Q 2731 : # self.tags.map { |t|
#   
#   t.hotness_mod
# }.sum
Query(Tag)
.where("story_id = ?")
# Q 2732 : # self.tags.map { |t|
#   
#   t.hotness_mod
# }.sum
Query(Tag)
.where("story_id = ?")
# Q 2733 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 2734 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 2735 : # self.tags.map { |t|
#   
#   t.hotness_mod
# }.sum
Query(Tag)
.where("story_id = ?")
# Q 2736 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 2737 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 2738 : # self.generated_markeddown_comment
Query(Comment)

# Q 2739 : # self.generated_markeddown_comment
Query(Comment)

# Q 2740 : # self.generated_markeddown_comment
Query(Comment)

# Q 2741 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 2742 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 2743 : # self.received_messages.each do |m|
#   
#   m.deleted_by_recipient = true
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 2744 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 2745 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 2746 : # story.downvotes
Query(Story)
.select('downvotes')
# Q 2747 : # @user.is_moderator?
Query(User)

# Q 2748 : # @user.can_downvote?(comment)
Query(User)

# Q 2749 : # @user.can_downvote?
Query(User)

# Q 2750 : # @user.can_downvote?
Query(User)

# Q 2751 : # story.downvotes
Query(Story)
.select('downvotes')
# Q 2752 : # story.score
Query(Story)

# Q 2753 : # @story.can_have_suggestions_from_user?(@user)
Query(Story)

# Q 2754 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 2755 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 2756 : # story.vote_summary_for(@user).downcase
Query(Story)

# Q 2757 : # story.vote_summary_for
Query(Story)

# Q 2758 : # @story.comments_path
Query(Story)

# Q 2759 : # @story.comments_path
Query(Story)

# Q 2760 : # self.invitations.destroy_all
Query(Invitation)
.where("user_id = ?")
# Q 2761 : # self.invitations
Query(Invitation)
.where("user_id = ?")
# Q 2762 : # self.invitations.destroy_all
Query(Invitation)
.where("user_id = ?")
# Q 2763 : # self.invitations.destroy_all
Query(Invitation)
.where("user_id = ?")
# Q 2764 : # self.invitations
Query(Invitation)
.where("user_id = ?")
# Q 2765 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   c.upvotes + 1 - c.downvotes
# }.inject(&:+).to_f
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2766 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   c.upvotes + 1 - c.downvotes
# }.inject(&:+)
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2767 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   c.upvotes + 1 - c.downvotes
# }.inject
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2768 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2769 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes)
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2770 : # self.comments.where("user_id <> ?", self.user_id).select
Query(Comment)
.where("story_id = ?")
.where(" = ?")
# Q 2771 : # self.comments.where("user_id <> ?", self.user_id)
Query(Comment)
.where("story_id = ?")
.where(" = ?")
# Q 2772 : # self.comments.where
Query(Comment)
.where("story_id = ?")
# Q 2773 : # self.comments
Query(Comment)
.where("story_id = ?")
# Q 2774 : # self.user_id
Query(Story)
.select('user_id')
# Q 2775 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   c.upvotes + 1 - c.downvotes
# }.inject(&:+).to_f
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2776 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   c.upvotes + 1 - c.downvotes
# }.inject
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2777 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 2778 : # self.comments.where("user_id <> ?", self.user_id).select
Query(Comment)
.where("story_id = ?")
.where(" = ?")
# Q 2779 : # self.comments.where
Query(Comment)
.where("story_id = ?")
# Q 2780 : # self.comments
Query(Comment)
.where("story_id = ?")
# Q 2781 : # self.user_id
Query(Story)
.select('user_id')
# Q 2782 : # @user.upvoted_stories.order("votes.id DESC")
Query(User)
.where("user_id = ?")
.order('id')
.order('id')
# Q 2783 : # @user.upvoted_stories.order
Query(User)
.where("user_id = ?")
# Q 2784 : # @user.upvoted_stories
Query(User)
.where("user_id = ?")
# Q 2785 : # @user.upvoted_stories.order
Query(User)
.where("user_id = ?")
# Q 2786 : # @user.upvoted_stories
Query(User)
.where("user_id = ?")
# Q 2787 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, comment.story_id, comment.id, @user.id, params[:reason])
Query(Vote)

# Q 2788 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2789 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2790 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2791 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2792 : # comment.id
Query(Comment)

# Q 2793 : # @user.id
Query(User)

# Q 2794 : # comment.id
Query(Comment)

# Q 2795 : # @user.id
Query(User)

# Q 2796 : # user.is_moderator?
Query(User)

# Q 2797 : # user.id
Query(User)

# Q 2798 : # self.user_id
Query(Comment)
.select('user_id')
# Q 2799 : # user.is_moderator?
Query(User)

# Q 2800 : # user.id
Query(User)

# Q 2801 : # self.user_id
Query(Comment)
.select('user_id')
# Q 2802 : # @story.dup
Query(Story)

# Q 2803 : # @story.dup
Query(Story)

# Q 2804 : # @story.dup
Query(Story)

# Q 2805 : # self.check_session_token
Query(User)

# Q 2806 : # self.check_session_token
Query(User)

# Q 2807 : # self.check_session_token
Query(User)

# Q 2808 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2809 : # Moderation.new
Query(Moderation)

# Q 2810 : # Moderation.new
Query(Moderation)

# Q 2811 : # Moderation.new
Query(Moderation)

# Q 2812 : # @story.valid?
Query(Story)

# Q 2813 : # @story.valid?
Query(Story)

# Q 2814 : # story.comments_path
Query(Story)

# Q 2815 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2816 : # self.id
Query(Comment)

# Q 2817 : # self.id
Query(Comment)

# Q 2818 : # self.id
Query(Comment)

# Q 2819 : # self.save!
Query(User)

# Q 2820 : # self.save!
Query(User)

# Q 2821 : # self.save!
Query(User)

# Q 2822 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject(&:+).to_f
Query(Story)
.where("story_id = ?")
# Q 2823 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject(&:+)
Query(Story)
.where("story_id = ?")
# Q 2824 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject
Query(Story)
.where("story_id = ?")
# Q 2825 : # self.merged_stories.map
Query(Story)
.where("story_id = ?")
# Q 2826 : # self.merged_stories
Query(Story)
.where("story_id = ?")
# Q 2827 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject(&:+).to_f
Query(Story)
.where("story_id = ?")
# Q 2828 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject
Query(Story)
.where("story_id = ?")
# Q 2829 : # self.merged_stories.map
Query(Story)
.where("story_id = ?")
# Q 2830 : # self.merged_stories
Query(Story)
.where("story_id = ?")
# Q 2831 : # user.id
Query(User)

# Q 2832 : # user.id
Query(User)

# Q 2833 : # user.id
Query(User)

# Q 2834 : # @story.title
Query(Story)
.select('title')
# Q 2835 : # @story.title
Query(Story)
.select('title')
# Q 2836 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2837 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2838 : # @story.save_suggested_title_for_user!(@story.title, @user)
Query(Story)

# Q 2839 : # @story.save_suggested_title_for_user!
Query(Story)

# Q 2840 : # @story.title
Query(Story)
.select('title')
# Q 2841 : # @story.save_suggested_title_for_user!
Query(Story)

# Q 2842 : # @story.title
Query(Story)
.select('title')
# Q 2843 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2844 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2845 : # User.transaction
Query(User)

# Q 2846 : # User.transaction
Query(User)

# Q 2847 : # self.comments.each
Query(Comment)
.where("user_id = ?")
# Q 2848 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 2849 : # self.comments.each { |c|
#   
#   c.undelete_for_user(self)
# }
Query(Comment)
.where("user_id = ?")
# Q 2850 : # self.comments.each
Query(Comment)
.where("user_id = ?")
# Q 2851 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 2852 : # @story.tags_a.sort
Query(Story)

# Q 2853 : # @story.tags_a
Query(Story)

# Q 2854 : # @story.tags_a.sort
Query(Story)

# Q 2855 : # @story.tags_a
Query(Story)

# Q 2856 : # @user.username
Query(User)
.select('username')
# Q 2857 : # @user.username
Query(User)
.select('username')
# Q 2858 : # @user.username
Query(User)
.select('username')
# Q 2859 : # @user.username
Query(User)
.select('username')
# Q 2860 : # @user.username
Query(User)
.select('username')
# Q 2861 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 2862 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 2863 : # self.sent_messages.each do |m|
#   
#   m.deleted_by_author = false
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 2864 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 2865 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 2866 : # @story.save_suggested_tags_a_for_user!(sugtags, @user)
Query(Story)

# Q 2867 : # @story.save_suggested_tags_a_for_user!
Query(Story)

# Q 2868 : # @story.save_suggested_tags_a_for_user!
Query(Story)

# Q 2869 : # self.save(:validate => false)
Query(Comment)

# Q 2870 : # self.save
Query(Comment)

# Q 2871 : # self.save
Query(Comment)

# Q 2872 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 2873 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 2874 : # self.received_messages.each do |m|
#   
#   m.deleted_by_recipient = false
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 2875 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 2876 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 2877 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes(:user, :story)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
.return_limit('')
.includes('user')
.includes('story')
# Q 2878 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes(:user, :story)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
.return_limit('')
.includes('user')
.includes('story')
# Q 2879 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
.return_limit('')
# Q 2880 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
.return_limit('')
# Q 2881 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
.return_limit('')
# Q 2882 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
# Q 2883 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
# Q 2884 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC")
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
# Q 2885 : # Comment.where(:is_deleted => false, :is_moderated => false).order
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
# Q 2886 : # Comment.where(:is_deleted => false, :is_moderated => false)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
# Q 2887 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
.return_limit('')
# Q 2888 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
.return_limit('')
# Q 2889 : # Comment.where(:is_deleted => false, :is_moderated => false).order("created_at DESC").offset
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('created_at')
# Q 2890 : # Comment.where(:is_deleted => false, :is_moderated => false).order
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
# Q 2891 : # self.created_at
Query(Story)
.select('created_at')
# Q 2892 : # self.created_at
Query(Story)
.select('created_at')
# Q 2893 : # @story.reload
Query(Story)

# Q 2894 : # @story.reload
Query(Story)

# Q 2895 : # @story.reload
Query(Story)

# Q 2896 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 2897 : # self.story
Query(Story)
.where("id = ?")
# Q 2898 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 2899 : # self.story
Query(Story)
.where("id = ?")
# Q 2900 : # user.is_moderator?
Query(User)

# Q 2901 : # user.id
Query(User)

# Q 2902 : # self.user_id
Query(Story)
.select('user_id')
# Q 2903 : # user.is_moderator?
Query(User)

# Q 2904 : # user.id
Query(User)

# Q 2905 : # self.user_id
Query(Story)
.select('user_id')
# Q 2906 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq.each
Query(Comment)
.distinct('')
# Q 2907 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq
Query(Comment)
.distinct('')
# Q 2908 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten
Query(Comment)

# Q 2909 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/)
Query(Comment)

# Q 2910 : # self.plaintext_comment.scan
Query(Comment)

# Q 2911 : # self.plaintext_comment
Query(Comment)

# Q 2912 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq.each
Query(Comment)
.distinct('')
# Q 2913 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq
Query(Comment)
.distinct('')
# Q 2914 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten
Query(Comment)

# Q 2915 : # self.plaintext_comment.scan
Query(Comment)

# Q 2916 : # self.plaintext_comment
Query(Comment)

# Q 2917 : # self.save!
Query(User)

# Q 2918 : # self.save!
Query(User)

# Q 2919 : # self.save!
Query(User)

# Q 2920 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2921 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2922 : # User.where(:username => mention)
Query(User)
.where("username = ?")
# Q 2923 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2924 : # User.where(:username => mention)
Query(User)
.where("username = ?")
# Q 2925 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2926 : # @user.tag_filters.map
Query(TagFilter)
.where("user_id = ?")
# Q 2927 : # @user.tag_filters
Query(TagFilter)
.where("user_id = ?")
# Q 2928 : # @user.tag_filters.map
Query(TagFilter)
.where("user_id = ?")
# Q 2929 : # @user.tag_filters
Query(TagFilter)
.where("user_id = ?")
# Q 2930 : # self.user.id
Query(User)
.where("id = ?")
# Q 2931 : # self.user
Query(User)
.where("id = ?")
# Q 2932 : # self.user.id
Query(User)
.where("id = ?")
# Q 2933 : # self.user
Query(User)
.where("id = ?")
# Q 2934 : # self.user.id
Query(User)
.where("id = ?")
# Q 2935 : # self.user
Query(User)
.where("id = ?")
# Q 2936 : # self.user.id
Query(User)
.where("id = ?")
# Q 2937 : # self.user
Query(User)
.where("id = ?")
# Q 2938 : # User.transaction
Query(User)

# Q 2939 : # User.transaction
Query(User)

# Q 2940 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 2941 : # @story.is_editable_by_user?
Query(Story)

# Q 2942 : # @story.is_editable_by_user?
Query(Story)

# Q 2943 : # @story.is_undeletable_by_user?(@user)
Query(Story)

# Q 2944 : # @story.is_undeletable_by_user?
Query(Story)

# Q 2945 : # @story.is_undeletable_by_user?
Query(Story)

# Q 2946 : # self.save!
Query(User)

# Q 2947 : # self.save!
Query(User)

# Q 2948 : # self.save!
Query(User)

# Q 2949 : # user.id
Query(User)

# Q 2950 : # self.user_id
Query(Story)
.select('user_id')
# Q 2951 : # user.can_offer_suggestions?
Query(User)

# Q 2952 : # user.id
Query(User)

# Q 2953 : # self.user_id
Query(Story)
.select('user_id')
# Q 2954 : # user.can_offer_suggestions?
Query(User)

# Q 2955 : # StoryRepository.new(@user, exclude_tags: filtered_tag_ids)
Query(StoryRepository)

# Q 2956 : # StoryRepository.new
Query(StoryRepository)

# Q 2957 : # StoryRepository.new
Query(StoryRepository)

# Q 2958 : # @user.id
Query(User)

# Q 2959 : # @user.id
Query(User)

# Q 2960 : # Moderation.new
Query(Moderation)

# Q 2961 : # Moderation.new
Query(Moderation)

# Q 2962 : # m = Moderation.new
Query(Moderation)

# Q 2963 : # Moderation.new
Query(Moderation)

# Q 2964 : # user.id
Query(User)

# Q 2965 : # user.id
Query(User)

# Q 2966 : # user.id
Query(User)

# Q 2967 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, @comments.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 2968 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, @comments.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 2969 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2970 : # @user.id
Query(User)

# Q 2971 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2972 : # @user.id
Query(User)

# Q 2973 : # self.id
Query(User)

# Q 2974 : # self.id
Query(User)

# Q 2975 : # self.id
Query(User)

# Q 2976 : # self.tags.select { |t|
#   
#   t.privileged?
# }.any?
Query(Tag)
.where("story_id = ?")
# Q 2977 : # self.tags.select
Query(Tag)
.where("story_id = ?")
# Q 2978 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 2979 : # self.tags.select { |t|
#   
#   t.privileged?
# }.any?
Query(Tag)
.where("story_id = ?")
# Q 2980 : # self.tags.select
Query(Tag)
.where("story_id = ?")
# Q 2981 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 2982 : # @comments.map
Query(Comment)

# Q 2983 : # @comments.map
Query(Comment)

# Q 2984 : # @story.save(:validate => false)
Query(Story)

# Q 2985 : # @story.save
Query(Story)

# Q 2986 : # @story.save
Query(Story)

# Q 2987 : # @comments.each
Query(Comment)

# Q 2988 : # @comments.each
Query(Comment)

# Q 2989 : # Hat.new
Query(Hat)

# Q 2990 : # Hat.new
Query(Hat)

# Q 2991 : # h = Hat.new
Query(Hat)

# Q 2992 : # Hat.new
Query(Hat)

# Q 2993 : # @story.comments_path
Query(Story)

# Q 2994 : # @story.comments_path
Query(Story)

# Q 2995 : # self.id
Query(User)

# Q 2996 : # self.id
Query(User)

# Q 2997 : # self.id
Query(User)

# Q 2998 : # StoriesPaginator.new(scope, page, @user).get
Query(StoriesPaginator)

# Q 2999 : # StoriesPaginator.new(scope, page, @user)
Query(StoriesPaginator)

# Q 3000 : # StoriesPaginator.new
Query(StoriesPaginator)

# Q 3001 : # StoriesPaginator.new(scope, page, @user).get
Query(StoriesPaginator)

# Q 3002 : # StoriesPaginator.new
Query(StoriesPaginator)

# Q 3003 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3004 : # self.user
Query(User)
.where("id = ?")
# Q 3005 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3006 : # self.story
Query(Story)
.where("id = ?")
# Q 3007 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3008 : # self.user
Query(User)
.where("id = ?")
# Q 3009 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3010 : # self.story
Query(Story)
.where("id = ?")
# Q 3011 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3012 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3013 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3014 : # self.user
Query(User)
.where("id = ?")
# Q 3015 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3016 : # self.story
Query(Story)
.where("id = ?")
# Q 3017 : # user.id
Query(User)

# Q 3018 : # user.id
Query(User)

# Q 3019 : # user.id
Query(User)

# Q 3020 : # self.plaintext_comment
Query(Comment)

# Q 3021 : # self.plaintext_comment
Query(Comment)

# Q 3022 : # self.plaintext_comment
Query(Comment)

# Q 3023 : # self.url
Query(Comment)

# Q 3024 : # self.url
Query(Comment)

# Q 3025 : # self.url
Query(Comment)

# Q 3026 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 3027 : # @story.is_editable_by_user?
Query(Story)

# Q 3028 : # @story.is_editable_by_user?
Query(Story)

# Q 3029 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3030 : # self.user
Query(User)
.where("id = ?")
# Q 3031 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3032 : # self.user
Query(User)
.where("id = ?")
# Q 3033 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3034 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3035 : # self.user
Query(User)
.where("id = ?")
# Q 3036 : # self.editor
Query(Story)

# Q 3037 : # self.user
Query(User)
.where("id = ?")
# Q 3038 : # self.editor
Query(Story)

# Q 3039 : # self.user
Query(User)
.where("id = ?")
# Q 3040 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 3041 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3042 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 3043 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3044 : # @user.username
Query(User)
.select('username')
# Q 3045 : # @user.username
Query(User)
.select('username')
# Q 3046 : # @user.username
Query(User)
.select('username')
# Q 3047 : # @user.username
Query(User)
.select('username')
# Q 3048 : # @user.username
Query(User)
.select('username')
# Q 3049 : # self.save!
Query(User)

# Q 3050 : # self.save!
Query(User)

# Q 3051 : # @story.url_is_editable_by_user?(@user)
Query(Story)

# Q 3052 : # @story.url_is_editable_by_user?
Query(Story)

# Q 3053 : # @story.url_is_editable_by_user?
Query(Story)

# Q 3054 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 3055 : # self.parent_comment.try(:user)
Query(Comment)
.where("id = ?")
.select('user')
# Q 3056 : # self.parent_comment.try(:user)
Query(Comment)
.where("id = ?")
.select('user')
# Q 3057 : # self.parent_comment.try
Query(Comment)
.where("id = ?")
# Q 3058 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 3059 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 3060 : # self.parent_comment.try
Query(Comment)
.where("id = ?")
# Q 3061 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 3062 : # self.user.id
Query(User)
.where("id = ?")
# Q 3063 : # self.user
Query(User)
.where("id = ?")
# Q 3064 : # self.user.id
Query(User)
.where("id = ?")
# Q 3065 : # self.user
Query(User)
.where("id = ?")
# Q 3066 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction? || t.tag.is_media?
# }.any?
Query(Tagging)
.where("story_id = ?")
# Q 3067 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3068 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3069 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction? || t.tag.is_media?
# }.any?
Query(Tagging)
.where("story_id = ?")
# Q 3070 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3071 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3072 : # @story.save
Query(Story)

# Q 3073 : # @story.save
Query(Story)

# Q 3074 : # @story.comments_path
Query(Story)

# Q 3075 : # @story.comments_path
Query(Story)

# Q 3076 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3077 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3078 : # User.where(:username => params[:user])
Query(User)
.where("username = ?")
# Q 3079 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3080 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3081 : # self.user
Query(User)
.where("id = ?")
# Q 3082 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3083 : # self.story
Query(Story)
.where("id = ?")
# Q 3084 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3085 : # self.user
Query(User)
.where("id = ?")
# Q 3086 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3087 : # self.story
Query(Story)
.where("id = ?")
# Q 3088 : # self.created_at
Query(User)
.select('created_at')
# Q 3089 : # self.created_at
Query(User)
.select('created_at')
# Q 3090 : # self.plaintext_comment
Query(Comment)

# Q 3091 : # self.plaintext_comment
Query(Comment)

# Q 3092 : # self.title_as_url
Query(Story)

# Q 3093 : # self.title_as_url
Query(Story)

# Q 3094 : # self.url
Query(Comment)

# Q 3095 : # self.url
Query(Comment)

# Q 3096 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3097 : # self.user
Query(User)
.where("id = ?")
# Q 3098 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3099 : # self.user
Query(User)
.where("id = ?")
# Q 3100 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, story.id, nil, @user.id, nil)
Query(Vote)

# Q 3101 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3102 : # story.id
Query(Story)

# Q 3103 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3104 : # story.id
Query(Story)

# Q 3105 : # self.title_as_url
Query(Story)

# Q 3106 : # self.title_as_url
Query(Story)

# Q 3107 : # @user.id
Query(User)

# Q 3108 : # @user.id
Query(User)

# Q 3109 : # self.about
Query(User)
.select('about')
# Q 3110 : # self.about
Query(User)
.select('about')
# Q 3111 : # @user.id
Query(User)

# Q 3112 : # @user.id
Query(User)

# Q 3113 : # Comment.where(:thread_id => thread_ids).includes(:user, :story).arrange_for_user(@showing_user)
Query(Comment)
.where("thread_id = ?")
.includes('user')
.includes('story')
# Q 3114 : # Comment.where(:thread_id => thread_ids).includes(:user, :story).arrange_for_user(@showing_user)
Query(Comment)
.where("thread_id = ?")
.includes('user')
.includes('story')
# Q 3115 : # Comment.where(:thread_id => thread_ids).includes(:user, :story).arrange_for_user
Query(Comment)
.where("thread_id = ?")
.includes('user')
.includes('story')
# Q 3116 : # Comment.where(:thread_id => thread_ids).includes(:user, :story)
Query(Comment)
.where("thread_id = ?")
.includes('user')
.includes('story')
# Q 3117 : # Comment.where(:thread_id => thread_ids).includes
Query(Comment)
.where("thread_id = ?")
# Q 3118 : # Comment.where(:thread_id => thread_ids)
Query(Comment)
.where("thread_id = ?")
# Q 3119 : # Comment.where(:thread_id => thread_ids).includes(:user, :story).arrange_for_user
Query(Comment)
.where("thread_id = ?")
.includes('user')
.includes('story')
# Q 3120 : # Comment.where(:thread_id => thread_ids).includes
Query(Comment)
.where("thread_id = ?")
# Q 3121 : # self.comment
Query(Comment)
.select('comment')
# Q 3122 : # self.comment
Query(Comment)
.select('comment')
# Q 3123 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order("COUNT(*) desc").first
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
.order('id')
.return_limit('1')
# Q 3124 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order("COUNT(*) desc")
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
.order('id')
# Q 3125 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 3126 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id])
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 3127 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 3128 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id })
Query(Tag)
.joins('stories')
.where("user_id = ?")
# Q 3129 : # Tag.active.joins(:stories).where
Query(Tag)
.joins('stories')
# Q 3130 : # Tag.active.joins(:stories)
Query(Tag)
.joins('stories')
# Q 3131 : # Tag.active.joins
Query(Tag)

# Q 3132 : # Tag.active
Query(Tag)

# Q 3133 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order("COUNT(*) desc").first
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
.order('id')
.return_limit('1')
# Q 3134 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 3135 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 3136 : # Tag.active.joins(:stories).where
Query(Tag)
.joins('stories')
# Q 3137 : # Tag.active.joins
Query(Tag)

# Q 3138 : # Tag.active
Query(Tag)

# Q 3139 : # self.generated_markeddown_description
Query(Story)

# Q 3140 : # self.generated_markeddown_description
Query(Story)

# Q 3141 : # self.generated_markeddown_description
Query(Story)

# Q 3142 : # self.id
Query(User)

# Q 3143 : # self.id
Query(User)

# Q 3144 : # self.description.present?
Query(Story)
.select('description')
# Q 3145 : # self.description
Query(Story)
.select('description')
# Q 3146 : # self.description.present?
Query(Story)
.select('description')
# Q 3147 : # self.description
Query(Story)
.select('description')
# Q 3148 : # Tag.arel_table
Query(Tag)

# Q 3149 : # Tag.arel_table
Query(Tag)

# Q 3150 : # self.markeddown_description.gsub(/<[^>]*>/, "")
Query(Story)
.select('markeddown_description')
# Q 3151 : # self.markeddown_description.gsub
Query(Story)
.select('markeddown_description')
# Q 3152 : # self.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 3153 : # self.markeddown_description.gsub
Query(Story)
.select('markeddown_description')
# Q 3154 : # self.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 3155 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, story.id, nil, @user.id, nil)
Query(Vote)

# Q 3156 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3157 : # story.id
Query(Story)

# Q 3158 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3159 : # story.id
Query(Story)

# Q 3160 : # @user.id
Query(User)

# Q 3161 : # @user.id
Query(User)

# Q 3162 : # comments.group_by(&:thread_id)
Query(Comment)

# Q 3163 : # comments.group_by(&:thread_id)
Query(Comment)

# Q 3164 : # comments.group_by
Query(Comment)

# Q 3165 : # comments.group_by
Query(Comment)

# Q 3166 : # Comment.connection.execute
Query(Comment)

# Q 3167 : # Comment.connection
Query(Comment)

# Q 3168 : # Comment.table_name
Query(Comment)

# Q 3169 : # Comment.connection.execute
Query(Comment)

# Q 3170 : # Comment.connection
Query(Comment)

# Q 3171 : # Comment.table_name
Query(Comment)

# Q 3172 : # self.story_cache
Query(Story)
.select('story_cache')
# Q 3173 : # self.story_cache
Query(Story)
.select('story_cache')
# Q 3174 : # @user.id
Query(User)

# Q 3175 : # @user.id
Query(User)

# Q 3176 : # self.calculated_confidence
Query(Comment)

# Q 3177 : # self.calculated_confidence
Query(Comment)

# Q 3178 : # Vote.comment_votes_by_user_for_story_hash(@user.id, comments.map(&:story_id).uniq)
Query(Vote)

# Q 3179 : # Vote.comment_votes_by_user_for_story_hash(@user.id, comments.map(&:story_id).uniq)
Query(Vote)

# Q 3180 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3181 : # @user.id
Query(User)

# Q 3182 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3183 : # @user.id
Query(User)

# Q 3184 : # self.id.to_i
Query(Comment)

# Q 3185 : # self.id
Query(Comment)

# Q 3186 : # self.id.to_i
Query(Comment)

# Q 3187 : # self.id
Query(Comment)

# Q 3188 : # comments.map(&:story_id).uniq
Query(Comment)
.distinct('')
# Q 3189 : # comments.map(&:story_id)
Query(Comment)

# Q 3190 : # comments.map
Query(Comment)

# Q 3191 : # comments.map(&:story_id).uniq
Query(Comment)
.distinct('')
# Q 3192 : # comments.map
Query(Comment)

# Q 3193 : # self.pushover_user_key.present?
Query(User)
.select('pushover_user_key')
# Q 3194 : # self.pushover_user_key
Query(User)
.select('pushover_user_key')
# Q 3195 : # self.pushover_user_key.present?
Query(User)
.select('pushover_user_key')
# Q 3196 : # self.pushover_user_key
Query(User)
.select('pushover_user_key')
# Q 3197 : # self.story.recalculate_hotness!
Query(Story)
.where("id = ?")
# Q 3198 : # self.story
Query(Story)
.where("id = ?")
# Q 3199 : # self.story.recalculate_hotness!
Query(Story)
.where("id = ?")
# Q 3200 : # self.story
Query(Story)
.where("id = ?")
# Q 3201 : # self.pushover_user_key
Query(User)
.select('pushover_user_key')
# Q 3202 : # self.pushover_user_key
Query(User)
.select('pushover_user_key')
# Q 3203 : # comments.each
Query(Comment)

# Q 3204 : # comments.each
Query(Comment)

# Q 3205 : # self.is_moderated?
Query(Comment)

# Q 3206 : # self.is_moderated?
Query(Comment)

# Q 3207 : # self.comments.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck(:thread_id)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
.select('thread_id')
# Q 3208 : # self.comments.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck(:thread_id)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
.select('thread_id')
# Q 3209 : # self.comments.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3210 : # self.comments.group(:thread_id).order("MAX(created_at) DESC").limit(amount)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3211 : # self.comments.group(:thread_id).order("MAX(created_at) DESC").limit
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3212 : # self.comments.group(:thread_id).order("MAX(created_at) DESC")
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
# Q 3213 : # self.comments.group(:thread_id).order
Query(Comment)
.where("user_id = ?")
.group('thread_id')
# Q 3214 : # self.comments.group(:thread_id)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
# Q 3215 : # self.comments.group
Query(Comment)
.where("user_id = ?")
.group('')
# Q 3216 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3217 : # self.comments.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3218 : # self.comments.group(:thread_id).order("MAX(created_at) DESC").limit
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3219 : # self.comments.group(:thread_id).order
Query(Comment)
.where("user_id = ?")
.group('thread_id')
# Q 3220 : # self.comments.group
Query(Comment)
.where("user_id = ?")
.group('')
# Q 3221 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3222 : # self.moderation.try(:moderator).try(:username).to_s
Query(Moderation)
.where("id = ?")
.select('moderator')
.select('username')
# Q 3223 : # self.moderation.try(:moderator).try(:username)
Query(Moderation)
.where("id = ?")
.select('moderator')
.select('username')
# Q 3224 : # self.moderation.try(:moderator).try
Query(Moderation)
.where("id = ?")
.select('moderator')
# Q 3225 : # self.moderation.try(:moderator)
Query(Moderation)
.where("id = ?")
.select('moderator')
# Q 3226 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3227 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3228 : # self.moderation.try(:moderator).try(:username).to_s
Query(Moderation)
.where("id = ?")
.select('moderator')
.select('username')
# Q 3229 : # self.moderation.try(:moderator).try
Query(Moderation)
.where("id = ?")
.select('moderator')
# Q 3230 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3231 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3232 : # self.url.blank?
Query(Story)
.select('url')
# Q 3233 : # self.url
Query(Story)
.select('url')
# Q 3234 : # self.url.blank?
Query(Story)
.select('url')
# Q 3235 : # self.url
Query(Story)
.select('url')
# Q 3236 : # self.moderation.try(:reason)
Query(Moderation)
.where("id = ?")
.select('reason')
# Q 3237 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3238 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3239 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3240 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3241 : # @user.can_downvote?(story)
Query(User)

# Q 3242 : # @user.can_downvote?
Query(User)

# Q 3243 : # @user.can_downvote?
Query(User)

# Q 3244 : # self.user.is_banned?
Query(User)
.where("id = ?")
# Q 3245 : # self.user
Query(User)
.where("id = ?")
# Q 3246 : # self.user.is_banned?
Query(User)
.where("id = ?")
# Q 3247 : # self.user
Query(User)
.where("id = ?")
# Q 3248 : # self.show_submitted_story_threads
Query(User)
.select('show_submitted_story_threads')
# Q 3249 : # self.show_submitted_story_threads
Query(User)
.select('show_submitted_story_threads')
# Q 3250 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount).pluck(:thread_id)
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
.select('thread_id')
# Q 3251 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount).pluck
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3252 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount)
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3253 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3254 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC")
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
# Q 3255 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
# Q 3256 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id)
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
# Q 3257 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('')
# Q 3258 : # Comment.joins(:story).where(:stories => { :user_id => self.id })
Query(Comment)
.joins('story')
.where("user_id = ?")
# Q 3259 : # Comment.joins(:story).where
Query(Comment)
.joins('story')
# Q 3260 : # Comment.joins(:story)
Query(Comment)
.joins('story')
# Q 3261 : # Comment.joins
Query(Comment)

# Q 3262 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount).pluck
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3263 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 3264 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
# Q 3265 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('')
# Q 3266 : # Comment.joins(:story).where
Query(Comment)
.joins('story')
# Q 3267 : # Comment.joins
Query(Comment)

# Q 3268 : # self.id
Query(User)

# Q 3269 : # self.id
Query(User)

# Q 3270 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "").gsub(/^www\d*\.(.+\..+)/, "\1")
Query(Story)
.select('url')
# Q 3271 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "").gsub
Query(Story)
.select('url')
# Q 3272 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "")
Query(Story)
.select('url')
# Q 3273 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub
Query(Story)
.select('url')
# Q 3274 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "")
Query(Story)
.select('url')
# Q 3275 : # self.url.gsub(/^[^:]+:\/\//, "").gsub
Query(Story)
.select('url')
# Q 3276 : # self.url.gsub(/^[^:]+:\/\//, "")
Query(Story)
.select('url')
# Q 3277 : # self.url.gsub
Query(Story)
.select('url')
# Q 3278 : # self.url
Query(Story)
.select('url')
# Q 3279 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "").gsub
Query(Story)
.select('url')
# Q 3280 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub
Query(Story)
.select('url')
# Q 3281 : # self.url.gsub(/^[^:]+:\/\//, "").gsub
Query(Story)
.select('url')
# Q 3282 : # self.url.gsub
Query(Story)
.select('url')
# Q 3283 : # self.url
Query(Story)
.select('url')
# Q 3284 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, story.id, nil, @user.id, params[:reason])
Query(Vote)

# Q 3285 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3286 : # story.id
Query(Story)

# Q 3287 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3288 : # story.id
Query(Story)

# Q 3289 : # @user.id
Query(User)

# Q 3290 : # @user.id
Query(User)

# Q 3291 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3292 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3293 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3294 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3295 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3296 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3297 : # Keystore.value_for
Query(Keystore)

# Q 3298 : # self.id
Query(User)

# Q 3299 : # Keystore.value_for
Query(Keystore)

# Q 3300 : # self.id
Query(User)

# Q 3301 : # self.domain
Query(Story)

# Q 3302 : # self.domain
Query(Story)

# Q 3303 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3304 : # self.user
Query(User)
.where("id = ?")
# Q 3305 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3306 : # self.user
Query(User)
.where("id = ?")
# Q 3307 : # HiddenStory.hide_story_for_user(story.id, @user.id)
Query(HiddenStory)

# Q 3308 : # HiddenStory.hide_story_for_user
Query(HiddenStory)

# Q 3309 : # story.id
Query(Story)

# Q 3310 : # @user.id
Query(User)

# Q 3311 : # HiddenStory.hide_story_for_user
Query(HiddenStory)

# Q 3312 : # story.id
Query(Story)

# Q 3313 : # @user.id
Query(User)

# Q 3314 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3315 : # self.user
Query(User)
.where("id = ?")
# Q 3316 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3317 : # self.user
Query(User)
.where("id = ?")
# Q 3318 : # self.url.present?
Query(Story)
.select('url')
# Q 3319 : # self.url
Query(Story)
.select('url')
# Q 3320 : # self.url.present?
Query(Story)
.select('url')
# Q 3321 : # self.url
Query(Story)
.select('url')
# Q 3322 : # self.story
Query(Story)
.where("id = ?")
# Q 3323 : # self.story.user_is_author?
Query(Story)
.where("id = ?")
# Q 3324 : # self.story
Query(Story)
.where("id = ?")
# Q 3325 : # self.story
Query(Story)
.where("id = ?")
# Q 3326 : # self.story.user_is_author?
Query(Story)
.where("id = ?")
# Q 3327 : # self.story
Query(Story)
.where("id = ?")
# Q 3328 : # self.url
Query(Story)
.select('url')
# Q 3329 : # self.url
Query(Story)
.select('url')
# Q 3330 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 3331 : # self.story
Query(Story)
.where("id = ?")
# Q 3332 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3333 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 3334 : # self.story
Query(Story)
.where("id = ?")
# Q 3335 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3336 : # self.description
Query(Story)
.select('description')
# Q 3337 : # self.description
Query(Story)
.select('description')
# Q 3338 : # self.save!
Query(User)

# Q 3339 : # self.save!
Query(User)

# Q 3340 : # HiddenStory.where(:user_id => @user.id, :story_id => story.id).delete_all
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3341 : # HiddenStory.where(:user_id => @user.id, :story_id => story.id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3342 : # @user.id
Query(User)

# Q 3343 : # story.id
Query(Story)

# Q 3344 : # HiddenStory.where(:user_id => @user.id, :story_id => story.id).delete_all
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3345 : # @user.id
Query(User)

# Q 3346 : # story.id
Query(Story)

# Q 3347 : # Comment.where(:short_id => params[:id]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 3348 : # Comment.where(:short_id => params[:id]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 3349 : # Comment.where(:short_id => params[:id])
Query(Comment)
.where("short_id = ?")
# Q 3350 : # Comment.where(:short_id => params[:id]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 3351 : # Moderation.new
Query(Moderation)

# Q 3352 : # Moderation.new
Query(Moderation)

# Q 3353 : # Moderation.new
Query(Moderation)

# Q 3354 : # user.is_moderator?
Query(User)

# Q 3355 : # user.is_moderator?
Query(User)

# Q 3356 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3357 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3358 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 3359 : # @user.id
Query(User)

# Q 3360 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3361 : # @user.id
Query(User)

# Q 3362 : # self.id
Query(User)

# Q 3363 : # self.id
Query(User)

# Q 3364 : # self.id
Query(User)

# Q 3365 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 3366 : # comment.id
Query(Comment)

# Q 3367 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 3368 : # comment.id
Query(Comment)

# Q 3369 : # user.id
Query(User)

# Q 3370 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3371 : # user.id
Query(User)

# Q 3372 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3373 : # Story.connection.execute
Query(Story)

# Q 3374 : # Story.connection
Query(Story)

# Q 3375 : # Story.table_name
Query(Story)

# Q 3376 : # Story.connection.execute
Query(Story)

# Q 3377 : # Story.connection
Query(Story)

# Q 3378 : # Story.table_name
Query(Story)

# Q 3379 : # self.calculated_hotness
Query(Story)

# Q 3380 : # self.id.to_i
Query(Story)

# Q 3381 : # self.id
Query(Story)

# Q 3382 : # self.calculated_hotness
Query(Story)

# Q 3383 : # self.id.to_i
Query(Story)

# Q 3384 : # self.id
Query(Story)

# Q 3385 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3386 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3387 : # HiddenStory.where(:story_id => self.id).count
Query(HiddenStory)
.where("story_id = ?")
# Q 3388 : # HiddenStory.where(:story_id => self.id)
Query(HiddenStory)
.where("story_id = ?")
# Q 3389 : # self.id
Query(Story)

# Q 3390 : # HiddenStory.where(:story_id => self.id).count
Query(HiddenStory)
.where("story_id = ?")
# Q 3391 : # self.id
Query(Story)

# Q 3392 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3393 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3394 : # @user.is_moderator?
Query(User)

# Q 3395 : # @user.is_moderator?
Query(User)

# Q 3396 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3397 : # self.user
Query(User)
.where("id = ?")
# Q 3398 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3399 : # self.user
Query(User)
.where("id = ?")
# Q 3400 : # Keystore.value_for
Query(Keystore)

# Q 3401 : # self.id
Query(User)

# Q 3402 : # Keystore.value_for
Query(Keystore)

# Q 3403 : # self.id
Query(User)

# Q 3404 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3405 : # self.user
Query(User)
.where("id = ?")
# Q 3406 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3407 : # self.user
Query(User)
.where("id = ?")
# Q 3408 : # user.id
Query(User)

# Q 3409 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3410 : # user.id
Query(User)

# Q 3411 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3412 : # self.is_moderated?
Query(Comment)

# Q 3413 : # self.is_moderated?
Query(Comment)

# Q 3414 : # self.user_is_author?
Query(Story)

# Q 3415 : # self.user_is_author?
Query(Story)

# Q 3416 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3417 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3418 : # Story.where(:short_id => params[:story_id])
Query(Story)
.where("short_id = ?")
# Q 3419 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3420 : # Keystore.put
Query(Keystore)

# Q 3421 : # self.id
Query(User)

# Q 3422 : # Keystore.put
Query(Keystore)

# Q 3423 : # self.id
Query(User)

# Q 3424 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try(:vote)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
.select('vote')
# Q 3425 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try(:vote)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
.select('vote')
# Q 3426 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3427 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3428 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 3429 : # @user.id
Query(User)

# Q 3430 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3431 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3432 : # @user.id
Query(User)

# Q 3433 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3434 : # self.updated_at.to_i
Query(Comment)
.select('updated_at')
# Q 3435 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3436 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3437 : # self.updated_at.to_i
Query(Comment)
.select('updated_at')
# Q 3438 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3439 : # self.received_messages.unread.count
Query(Message)
.where("user_id = ?")
# Q 3440 : # self.received_messages.unread
Query(Message)
.where("user_id = ?")
# Q 3441 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 3442 : # self.received_messages.unread.count
Query(Message)
.where("user_id = ?")
# Q 3443 : # self.received_messages.unread
Query(Message)
.where("user_id = ?")
# Q 3444 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 3445 : # story.id
Query(Story)

# Q 3446 : # story.id
Query(Story)

# Q 3447 : # self.created_at.to_i
Query(Comment)
.select('created_at')
# Q 3448 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3449 : # self.created_at.to_i
Query(Comment)
.select('created_at')
# Q 3450 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3451 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id").order("id DESC")
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
.order('id')
.order('id')
# Q 3452 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id").order
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 3453 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id")
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 3454 : # self.votes.joins(:story, :comment).where
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 3455 : # self.votes.joins(:story, :comment)
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 3456 : # self.votes.joins
Query(Vote)
.where("user_id = ?")
# Q 3457 : # self.votes
Query(Vote)
.where("user_id = ?")
# Q 3458 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id").order
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 3459 : # self.votes.joins(:story, :comment).where
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 3460 : # self.votes.joins
Query(Vote)
.where("user_id = ?")
# Q 3461 : # self.votes
Query(Vote)
.where("user_id = ?")
# Q 3462 : # self.created_at
Query(Story)
.select('created_at')
# Q 3463 : # self.created_at
Query(Story)
.select('created_at')
# Q 3464 : # self.created_at
Query(Story)
.select('created_at')
# Q 3465 : # self.created_at
Query(Story)
.select('created_at')
# Q 3466 : # user.is_moderator?
Query(User)

# Q 3467 : # user.is_moderator?
Query(User)

# Q 3468 : # user.is_moderator?
Query(User)

# Q 3469 : # user.is_moderator?
Query(User)

# Q 3470 : # @user.is_moderator?
Query(User)

# Q 3471 : # @user.is_moderator?
Query(User)

# Q 3472 : # user.id
Query(User)

# Q 3473 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3474 : # self.is_moderated?
Query(Comment)

# Q 3475 : # user.id
Query(User)

# Q 3476 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3477 : # self.is_moderated?
Query(Comment)

# Q 3478 : # Story.where(:short_id => params[:story_id] || params[:id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3479 : # Story.where(:short_id => params[:story_id] || params[:id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3480 : # Story.where(:short_id => params[:story_id] || params[:id])
Query(Story)
.where("short_id = ?")
# Q 3481 : # Story.where(:short_id => params[:story_id] || params[:id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3482 : # user.id
Query(User)

# Q 3483 : # self.user_id
Query(Story)
.select('user_id')
# Q 3484 : # user.id
Query(User)

# Q 3485 : # self.user_id
Query(Story)
.select('user_id')
# Q 3486 : # self.is_moderated?
Query(Story)

# Q 3487 : # self.is_moderated?
Query(Story)

# Q 3488 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id])).first
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 3489 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id])).first
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 3490 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id]))
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
# Q 3491 : # @user.id
Query(User)

# Q 3492 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id])).first
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 3493 : # @user.id
Query(User)

# Q 3494 : # self.created_at.to_i
Query(Story)
.select('created_at')
# Q 3495 : # self.created_at
Query(Story)
.select('created_at')
# Q 3496 : # self.created_at.to_i
Query(Story)
.select('created_at')
# Q 3497 : # self.created_at
Query(Story)
.select('created_at')
# Q 3498 : # Keystore.increment_value_for
Query(Keystore)

# Q 3499 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3500 : # Keystore.increment_value_for
Query(Keystore)

# Q 3501 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3502 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3503 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3504 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 3505 : # @user.id
Query(User)

# Q 3506 : # @story.id
Query(Story)

# Q 3507 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3508 : # @user.id
Query(User)

# Q 3509 : # @story.id
Query(Story)

# Q 3510 : # HiddenStory.where(:user_id => user.id, :story_id => self.id).first
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
.return_limit('1')
# Q 3511 : # HiddenStory.where(:user_id => user.id, :story_id => self.id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3512 : # user.id
Query(User)

# Q 3513 : # self.id
Query(Story)

# Q 3514 : # HiddenStory.where(:user_id => user.id, :story_id => self.id).first
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
.return_limit('1')
# Q 3515 : # user.id
Query(User)

# Q 3516 : # self.id
Query(Story)

# Q 3517 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3518 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3519 : # self.is_from_email
Query(Comment)
.select('is_from_email')
# Q 3520 : # self.is_from_email
Query(Comment)
.select('is_from_email')
# Q 3521 : # self.created_at
Query(Story)
.select('created_at')
# Q 3522 : # self.created_at
Query(Story)
.select('created_at')
# Q 3523 : # @story.is_hidden_by_user?(@user)
Query(Story)

# Q 3524 : # @story.is_hidden_by_user?(@user)
Query(Story)

# Q 3525 : # @story.is_hidden_by_user?
Query(Story)

# Q 3526 : # @story.is_hidden_by_user?
Query(Story)

# Q 3527 : # Vote.comment_votes_by_user_for_story_hash(@user.id, @story.id)
Query(Vote)

# Q 3528 : # Vote.comment_votes_by_user_for_story_hash(@user.id, @story.id)
Query(Vote)

# Q 3529 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3530 : # @user.id
Query(User)

# Q 3531 : # @story.id
Query(Story)

# Q 3532 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3533 : # @user.id
Query(User)

# Q 3534 : # @story.id
Query(Story)

# Q 3535 : # @comments.each
Query(Comment)

# Q 3536 : # @comments.each
Query(Comment)

# Q 3537 : # self.story.comments_path
Query(Story)
.where("id = ?")
# Q 3538 : # self.story
Query(Story)
.where("id = ?")
# Q 3539 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3540 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3541 : # self.story.comments_path
Query(Story)
.where("id = ?")
# Q 3542 : # self.story
Query(Story)
.where("id = ?")
# Q 3543 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3544 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3545 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 3546 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 3547 : # self.is_unavailable
Query(Story)

# Q 3548 : # self.is_unavailable
Query(Story)

# Q 3549 : # user.is_moderator?
Query(User)

# Q 3550 : # user.is_moderator?
Query(User)

# Q 3551 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, self.story_id, self.id, self.user_id, nil, false)
Query(Vote)

# Q 3552 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3553 : # self.story_id
Query(Comment)
.select('story_id')
# Q 3554 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3555 : # self.story_id
Query(Comment)
.select('story_id')
# Q 3556 : # self.id
Query(Comment)

# Q 3557 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3558 : # self.id
Query(Comment)

# Q 3559 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3560 : # user.id
Query(User)

# Q 3561 : # self.user_id
Query(Story)
.select('user_id')
# Q 3562 : # self.is_moderated?
Query(Story)

# Q 3563 : # user.id
Query(User)

# Q 3564 : # self.user_id
Query(Story)
.select('user_id')
# Q 3565 : # self.is_moderated?
Query(Story)

# Q 3566 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3567 : # self.story
Query(Story)
.where("id = ?")
# Q 3568 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3569 : # self.story
Query(Story)
.where("id = ?")
# Q 3570 : # self.upvotes
Query(Comment)
.select('upvotes')
# Q 3571 : # self.downvotes
Query(Comment)
.select('downvotes')
# Q 3572 : # self.upvotes
Query(Comment)
.select('upvotes')
# Q 3573 : # self.downvotes
Query(Comment)
.select('downvotes')
# Q 3574 : # self.new_record?
Query(Story)

# Q 3575 : # self.new_record?
Query(Story)

# Q 3576 : # self.editing_from_suggestions
Query(Story)

# Q 3577 : # self.editing_from_suggestions
Query(Story)

# Q 3578 : # self.story.short_id_path
Query(Story)
.where("id = ?")
# Q 3579 : # self.story
Query(Story)
.where("id = ?")
# Q 3580 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3581 : # self.story.short_id_path
Query(Story)
.where("id = ?")
# Q 3582 : # self.story
Query(Story)
.where("id = ?")
# Q 3583 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3584 : # self.editor
Query(Story)

# Q 3585 : # self.editor.id
Query(Story)

# Q 3586 : # self.editor
Query(Story)

# Q 3587 : # self.user_id
Query(Story)
.select('user_id')
# Q 3588 : # self.editor
Query(Story)

# Q 3589 : # self.editor.id
Query(Story)

# Q 3590 : # self.editor
Query(Story)

# Q 3591 : # self.user_id
Query(Story)
.select('user_id')
# Q 3592 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3593 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3594 : # self.changes.merge(self.tagging_changes)
Query(Story)

# Q 3595 : # self.changes.merge(self.tagging_changes)
Query(Story)

# Q 3596 : # self.changes.merge
Query(Story)

# Q 3597 : # self.changes
Query(Story)

# Q 3598 : # self.tagging_changes
Query(Story)

# Q 3599 : # self.changes.merge
Query(Story)

# Q 3600 : # self.changes
Query(Story)

# Q 3601 : # self.tagging_changes
Query(Story)

# Q 3602 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3603 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3604 : # Moderation.new
Query(Moderation)

# Q 3605 : # Moderation.new
Query(Moderation)

# Q 3606 : # Moderation.new
Query(Moderation)

# Q 3607 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3608 : # self.story
Query(Story)
.where("id = ?")
# Q 3609 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3610 : # self.story
Query(Story)
.where("id = ?")
# Q 3611 : # self.editing_from_suggestions
Query(Story)

# Q 3612 : # self.editing_from_suggestions
Query(Story)

# Q 3613 : # self.editor.try(:id)
Query(Story)
.select('id')
# Q 3614 : # self.editor.try(:id)
Query(Story)
.select('id')
# Q 3615 : # self.editor.try
Query(Story)

# Q 3616 : # self.editor
Query(Story)

# Q 3617 : # self.editor.try
Query(Story)

# Q 3618 : # self.editor
Query(Story)

# Q 3619 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 3620 : # self.story
Query(Story)
.where("id = ?")
# Q 3621 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3622 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3623 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 3624 : # self.story
Query(Story)
.where("id = ?")
# Q 3625 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3626 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3627 : # self.id
Query(Story)

# Q 3628 : # self.id
Query(Story)

# Q 3629 : # self.id
Query(Story)

# Q 3630 : # self.is_expired?
Query(Story)

# Q 3631 : # self.is_expired?
Query(Story)

# Q 3632 : # self.is_expired?
Query(Story)

# Q 3633 : # self.is_expired?
Query(Story)

# Q 3634 : # self.votes.includes(:user).each
Query(Vote)
.where("comment_id = ?")
.includes('user')
# Q 3635 : # self.votes.includes(:user)
Query(Vote)
.where("comment_id = ?")
.includes('user')
# Q 3636 : # self.votes.includes
Query(Vote)
.where("comment_id = ?")
# Q 3637 : # self.votes
Query(Vote)
.where("comment_id = ?")
# Q 3638 : # self.votes.includes(:user).each
Query(Vote)
.where("comment_id = ?")
.includes('user')
# Q 3639 : # self.votes.includes
Query(Vote)
.where("comment_id = ?")
# Q 3640 : # self.votes
Query(Vote)
.where("comment_id = ?")
# Q 3641 : # self.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 3642 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3643 : # self.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 3644 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3645 : # self.merged_into_story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3646 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3647 : # self.merged_into_story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3648 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3649 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3650 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3651 : # self.moderation_reason
Query(Story)

# Q 3652 : # self.moderation_reason
Query(Story)

# Q 3653 : # self.moderation_reason
Query(Story)

# Q 3654 : # user.is_moderator?
Query(User)

# Q 3655 : # user.is_moderator?
Query(User)

# Q 3656 : # Keystore.increment_value_for
Query(Keystore)

# Q 3657 : # self.user_id
Query(Story)
.select('user_id')
# Q 3658 : # Keystore.increment_value_for
Query(Keystore)

# Q 3659 : # self.user_id
Query(Story)
.select('user_id')
# Q 3660 : # user.id
Query(User)

# Q 3661 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3662 : # user.id
Query(User)

# Q 3663 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3664 : # Moderation.new
Query(Moderation)

# Q 3665 : # Moderation.new
Query(Moderation)

# Q 3666 : # Moderation.new
Query(Moderation)

# Q 3667 : # self.id
Query(Comment)

# Q 3668 : # self.id
Query(Comment)

# Q 3669 : # self.id
Query(Comment)

# Q 3670 : # user.id
Query(User)

# Q 3671 : # user.id
Query(User)

# Q 3672 : # user.id
Query(User)

# Q 3673 : # Comment.where(:story_id => Story.select(:id).where(:merged_story_id => self.id) + [self.id])
Query(Comment)
.where("story_id = ?")
# Q 3674 : # Story.select(:id).where(:merged_story_id => self.id)
Query(Story)
.select('id')
.where("merged_story_id = ?")
# Q 3675 : # Story.select(:id).where
Query(Story)
.select('id')
# Q 3676 : # Story.select(:id)
Query(Story)
.select('id')
# Q 3677 : # Story.select
Query(Story)

# Q 3678 : # Story.select(:id).where
Query(Story)
.select('id')
# Q 3679 : # Story.select
Query(Story)

# Q 3680 : # self.id
Query(Story)

# Q 3681 : # self.id
Query(Story)

# Q 3682 : # self.id
Query(Story)

# Q 3683 : # self.id
Query(Story)

# Q 3684 : # self.save(:validate => false)
Query(Comment)

# Q 3685 : # self.save
Query(Comment)

# Q 3686 : # self.save
Query(Comment)

# Q 3687 : # Story.where(:short_id => sid).first.id
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3688 : # Story.where(:short_id => sid).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3689 : # Story.where(:short_id => sid)
Query(Story)
.where("short_id = ?")
# Q 3690 : # Story.where(:short_id => sid).first.id
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3691 : # Story.where(:short_id => sid).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3692 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3693 : # self.story
Query(Story)
.where("id = ?")
# Q 3694 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3695 : # self.story
Query(Story)
.where("id = ?")
# Q 3696 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, self.id, nil, self.user_id, nil, false)
Query(Vote)

# Q 3697 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3698 : # self.id
Query(Story)

# Q 3699 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3700 : # self.id
Query(Story)

# Q 3701 : # self.user_id
Query(Story)
.select('user_id')
# Q 3702 : # self.user_id
Query(Story)
.select('user_id')
# Q 3703 : # self.title.to_s.split("").map { |chr|
#   
#   if chr.ord == 160
#     
#     " "
#   else
#     
#     chr
#   end
# }.join("")
Query(Story)
.select('title')
# Q 3704 : # self.title.to_s.split("").map { |chr|
#   
#   if chr.ord == 160
#     
#     " "
#   else
#     
#     chr
#   end
# }.join("")
Query(Story)
.select('title')
# Q 3705 : # self.title.to_s.split("").map { |chr|
#   
#   if chr.ord == 160
#     
#     " "
#   else
#     
#     chr
#   end
# }.join
Query(Story)
.select('title')
# Q 3706 : # self.title.to_s.split("").map
Query(Story)
.select('title')
# Q 3707 : # self.title.to_s.split("")
Query(Story)
.select('title')
# Q 3708 : # self.title.to_s.split
Query(Story)
.select('title')
# Q 3709 : # self.title.to_s
Query(Story)
.select('title')
# Q 3710 : # self.title
Query(Story)
.select('title')
# Q 3711 : # self.title.to_s.split("").map { |chr|
#   
#   if chr.ord == 160
#     
#     " "
#   else
#     
#     chr
#   end
# }.join
Query(Story)
.select('title')
# Q 3712 : # self.title.to_s.split("").map
Query(Story)
.select('title')
# Q 3713 : # self.title.to_s.split
Query(Story)
.select('title')
# Q 3714 : # self.title.to_s
Query(Story)
.select('title')
# Q 3715 : # self.title
Query(Story)
.select('title')
# Q 3716 : # self.short_id
Query(Story)
.select('short_id')
# Q 3717 : # self.short_id
Query(Story)
.select('short_id')
# Q 3718 : # self.short_id
Query(Story)
.select('short_id')
# Q 3719 : # self.short_id
Query(Story)
.select('short_id')
# Q 3720 : # self.taggings.sort_by { |t|
#   
#   t.tag.tag
# }.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 3721 : # self.taggings.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 3722 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3723 : # self.taggings.sort_by { |t|
#   
#   t.tag.tag
# }.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 3724 : # self.taggings.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 3725 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3726 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 3727 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 3728 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 3729 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 3730 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3731 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3732 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 3733 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 3734 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3735 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3736 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 3737 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 3738 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 3739 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 3740 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3741 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3742 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 3743 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 3744 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3745 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3746 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 3747 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3748 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3749 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 3750 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3751 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3752 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 3753 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3754 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 3755 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3756 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 3757 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 3758 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 3759 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 3760 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 3761 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 3762 : # tagging.mark_for_destruction
Query(Tagging)

# Q 3763 : # tagging.mark_for_destruction
Query(Tagging)

# Q 3764 : # tagging.mark_for_destruction
Query(Tagging)

# Q 3765 : # tagging.mark_for_destruction
Query(Tagging)

# Q 3766 : # self.tags.exists?(:tag => tag_name)
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 3767 : # self.tags.exists?
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 3768 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 3769 : # self.tags.exists?(:tag => tag_name)
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 3770 : # self.tags.exists?
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 3771 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 3772 : # self.tags.exists?
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 3773 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 3774 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3775 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3776 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 3777 : # Tag.active.where
Query(Tag)

# Q 3778 : # Tag.active
Query(Tag)

# Q 3779 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3780 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 3781 : # Tag.active.where
Query(Tag)

# Q 3782 : # Tag.active
Query(Tag)

# Q 3783 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3784 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 3785 : # Tag.active.where
Query(Tag)

# Q 3786 : # Tag.active
Query(Tag)

# Q 3787 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3788 : # Tag.active.where
Query(Tag)

# Q 3789 : # Tag.active
Query(Tag)

# Q 3790 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 3791 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 3792 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3793 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 3794 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3795 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 3796 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3797 : # tg = self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 3798 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 3799 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3800 : # self.suggested_taggings.where(:user_id => user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 3801 : # self.suggested_taggings.where(:user_id => user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 3802 : # self.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3803 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3804 : # user.id
Query(User)

# Q 3805 : # self.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3806 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3807 : # user.id
Query(User)

# Q 3808 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 3809 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 3810 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 3811 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 3812 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 3813 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 3814 : # tagging.destroy
Query(Tagging)

# Q 3815 : # tagging.destroy
Query(Tagging)

# Q 3816 : # tagging.destroy
Query(Tagging)

# Q 3817 : # tagging.destroy
Query(Tagging)

# Q 3818 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3819 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3820 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 3821 : # Tag.active.where
Query(Tag)

# Q 3822 : # Tag.active
Query(Tag)

# Q 3823 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3824 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 3825 : # Tag.active.where
Query(Tag)

# Q 3826 : # Tag.active
Query(Tag)

# Q 3827 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3828 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 3829 : # Tag.active.where
Query(Tag)

# Q 3830 : # Tag.active
Query(Tag)

# Q 3831 : # t = Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3832 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3833 : # Tag.active.where
Query(Tag)

# Q 3834 : # Tag.active
Query(Tag)

# Q 3835 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3836 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3837 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3838 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3839 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3840 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3841 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3842 : # tg = self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3843 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3844 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3845 : # user.id
Query(User)

# Q 3846 : # user.id
Query(User)

# Q 3847 : # user.id
Query(User)

# Q 3848 : # user.id
Query(User)

# Q 3849 : # user.id
Query(User)

# Q 3850 : # self.suggested_taggings.group_by(&:user_id).each
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3851 : # self.suggested_taggings.group_by(&:user_id)
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3852 : # self.suggested_taggings.group_by
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3853 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3854 : # self.suggested_taggings.group_by(&:user_id).each
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3855 : # self.suggested_taggings.group_by
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3856 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3857 : # self.tags_a.sort
Query(Story)

# Q 3858 : # self.tags_a
Query(Story)

# Q 3859 : # self.tags_a.sort
Query(Story)

# Q 3860 : # self.tags_a
Query(Story)

# Q 3861 : # self.id
Query(Story)

# Q 3862 : # self.id
Query(Story)

# Q 3863 : # self.tags_a.inspect
Query(Story)

# Q 3864 : # self.tags_a
Query(Story)

# Q 3865 : # self.tags_a.inspect
Query(Story)

# Q 3866 : # self.tags_a
Query(Story)

# Q 3867 : # self.save
Query(Story)

# Q 3868 : # self.save
Query(Story)

# Q 3869 : # self.id
Query(Story)

# Q 3870 : # self.id
Query(Story)

# Q 3871 : # self.errors.inspect
Query(Story)

# Q 3872 : # self.errors
Query(Story)

# Q 3873 : # self.errors.inspect
Query(Story)

# Q 3874 : # self.errors
Query(Story)

# Q 3875 : # self.suggested_titles.where(:user_id => user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 3876 : # self.suggested_titles.where(:user_id => user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 3877 : # self.suggested_titles.where(:user_id => user.id)
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
# Q 3878 : # self.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3879 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3880 : # user.id
Query(User)

# Q 3881 : # self.suggested_titles.where(:user_id => user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 3882 : # self.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3883 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3884 : # user.id
Query(User)

# Q 3885 : # self.suggested_titles.build
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3886 : # self.suggested_titles.build
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3887 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3888 : # self.suggested_titles.build
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3889 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3890 : # user.id
Query(User)

# Q 3891 : # user.id
Query(User)

# Q 3892 : # user.id
Query(User)

# Q 3893 : # self.suggested_titles.each
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3894 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3895 : # self.suggested_titles.each
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3896 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3897 : # self.id
Query(Story)

# Q 3898 : # self.id
Query(Story)

# Q 3899 : # self.id
Query(Story)

# Q 3900 : # self.id
Query(Story)

# Q 3901 : # self.title.inspect
Query(Story)
.select('title')
# Q 3902 : # self.title
Query(Story)
.select('title')
# Q 3903 : # self.title.inspect
Query(Story)
.select('title')
# Q 3904 : # self.title
Query(Story)
.select('title')
# Q 3905 : # self.title.inspect
Query(Story)
.select('title')
# Q 3906 : # self.title.inspect
Query(Story)
.select('title')
# Q 3907 : # self.title
Query(Story)
.select('title')
# Q 3908 : # self.save
Query(Story)

# Q 3909 : # self.save
Query(Story)

# Q 3910 : # self.save
Query(Story)

# Q 3911 : # self.save
Query(Story)

# Q 3912 : # self.id
Query(Story)

# Q 3913 : # self.id
Query(Story)

# Q 3914 : # self.id
Query(Story)

# Q 3915 : # self.id
Query(Story)

# Q 3916 : # self.id
Query(Story)

# Q 3917 : # self.errors.inspect
Query(Story)

# Q 3918 : # self.errors
Query(Story)

# Q 3919 : # self.errors.inspect
Query(Story)

# Q 3920 : # self.errors
Query(Story)

# Q 3921 : # self.errors.inspect
Query(Story)

# Q 3922 : # self.errors
Query(Story)

# Q 3923 : # self.errors.inspect
Query(Story)

# Q 3924 : # self.errors
Query(Story)

# Q 3925 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_").split("_").reject { |z|
#   
#   ["", "a", "an", "and", "but", "in", "of", "or", "that", "the", "to"].include?(z)
# }.each
Query(Story)
.select('title')
# Q 3926 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_").split("_").reject
Query(Story)
.select('title')
# Q 3927 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_").split("_")
Query(Story)
.select('title')
# Q 3928 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_").split
Query(Story)
.select('title')
# Q 3929 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_")
Query(Story)
.select('title')
# Q 3930 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub
Query(Story)
.select('title')
# Q 3931 : # self.title.downcase.gsub(/[,'`\"]/, "")
Query(Story)
.select('title')
# Q 3932 : # self.title.downcase.gsub
Query(Story)
.select('title')
# Q 3933 : # self.title.downcase
Query(Story)
.select('title')
# Q 3934 : # self.title
Query(Story)
.select('title')
# Q 3935 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_").split("_").reject { |z|
#   
#   ["", "a", "an", "and", "but", "in", "of", "or", "that", "the", "to"].include?(z)
# }.each
Query(Story)
.select('title')
# Q 3936 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_").split("_").reject
Query(Story)
.select('title')
# Q 3937 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub(/[^a-z0-9]/, "_").split
Query(Story)
.select('title')
# Q 3938 : # self.title.downcase.gsub(/[,'`\"]/, "").gsub
Query(Story)
.select('title')
# Q 3939 : # self.title.downcase.gsub
Query(Story)
.select('title')
# Q 3940 : # self.title.downcase
Query(Story)
.select('title')
# Q 3941 : # self.title
Query(Story)
.select('title')
# Q 3942 : # self.short_id
Query(Story)
.select('short_id')
# Q 3943 : # self.short_id
Query(Story)
.select('short_id')
# Q 3944 : # self.is_unavailable
Query(Story)

# Q 3945 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 3946 : # self.is_unavailable
Query(Story)

# Q 3947 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 3948 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 3949 : # self.is_unavailable
Query(Story)

# Q 3950 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 3951 : # self.is_unavailable
Query(Story)

# Q 3952 : # self.merged_comments.arrange_for_user(nil)
Query(Story)

# Q 3953 : # self.merged_comments.arrange_for_user(nil)
Query(Story)

# Q 3954 : # self.merged_comments.arrange_for_user
Query(Story)

# Q 3955 : # self.merged_comments
Query(Story)

# Q 3956 : # self.merged_comments.arrange_for_user
Query(Story)

# Q 3957 : # self.merged_comments
Query(Story)

# Q 3958 : # comments.count
Query(Comment)

# Q 3959 : # comments.count
Query(Comment)

# Q 3960 : # self.recalculate_hotness!
Query(Story)

# Q 3961 : # self.recalculate_hotness!
Query(Story)

# Q 3962 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3963 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3964 : # self.merged_into_story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3965 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3966 : # self.merged_into_story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3967 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 3968 : # self.new_record?
Query(Story)

# Q 3969 : # self.new_record?
Query(Story)

# Q 3970 : # user.is_moderator?
Query(User)

# Q 3971 : # self.url.present?
Query(Story)
.select('url')
# Q 3972 : # self.url
Query(Story)
.select('url')
# Q 3973 : # user.is_moderator?
Query(User)

# Q 3974 : # self.url.present?
Query(Story)
.select('url')
# Q 3975 : # self.url
Query(Story)
.select('url')
# Q 3976 : # self.url.blank?
Query(Story)
.select('url')
# Q 3977 : # self.url
Query(Story)
.select('url')
# Q 3978 : # self.comments_path
Query(Story)

# Q 3979 : # self.url
Query(Story)
.select('url')
# Q 3980 : # self.url.blank?
Query(Story)
.select('url')
# Q 3981 : # self.url
Query(Story)
.select('url')
# Q 3982 : # self.comments_path
Query(Story)

# Q 3983 : # self.url
Query(Story)
.select('url')
# Q 3984 : # self.url.blank?
Query(Story)
.select('url')
# Q 3985 : # self.url
Query(Story)
.select('url')
# Q 3986 : # self.comments_url
Query(Story)

# Q 3987 : # self.url
Query(Story)
.select('url')
# Q 3988 : # self.url.blank?
Query(Story)
.select('url')
# Q 3989 : # self.url
Query(Story)
.select('url')
# Q 3990 : # self.comments_url
Query(Story)

# Q 3991 : # self.url
Query(Story)
.select('url')
# Q 3992 : # Vote.where(:story_id => self.id, :comment_id => nil).where("vote != 0").each
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
.where(" = ?")
# Q 3993 : # Vote.where(:story_id => self.id, :comment_id => nil).where("vote != 0")
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
.where(" = ?")
# Q 3994 : # Vote.where(:story_id => self.id, :comment_id => nil).where
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
# Q 3995 : # Vote.where(:story_id => self.id, :comment_id => nil)
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
# Q 3996 : # self.id
Query(Story)

# Q 3997 : # Vote.where(:story_id => self.id, :comment_id => nil).where("vote != 0").each
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
.where(" = ?")
# Q 3998 : # Vote.where(:story_id => self.id, :comment_id => nil).where
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
# Q 3999 : # self.id
Query(Story)

# Q 4000 : # user.is_moderator?
Query(User)

# Q 4001 : # user.is_moderator?
Query(User)

# Q 4002 : # user.is_moderator?
Query(User)

# Q 4003 : # user.is_moderator?
Query(User)

# Q 4004 : # user.is_moderator?
Query(User)

# Q 4005 : # self.url
Query(Story)
.select('url')
# Q 4006 : # self.url
Query(Story)
.select('url')
# Q 4007 : # self.url
Query(Story)
.select('url')
# Q 4008 : # self.url
Query(Story)
.select('url')
# Q 4009 : # self.fetching_ip
Query(Story)

# Q 4010 : # self.fetching_ip
Query(Story)

