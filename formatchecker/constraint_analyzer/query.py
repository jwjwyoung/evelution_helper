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

# Q 16 : # story.errors.count
Query(Story)

# Q 17 : # story.errors
Query(Story)

# Q 18 : # story.already_posted_story
Query(Story)

# Q 19 : # comment.score
Query(Comment)

# Q 20 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 21 : # @user.id
Query(User)

# Q 22 : # @message.url
Query(Message)

# Q 23 : # @invitation_request.ip_address
Query(InvitationRequest)
.select('ip_address')
# Q 24 : # @comment.plaintext_comment
Query(Comment)

# Q 25 : # @comment.plaintext_comment
Query(Comment)

# Q 26 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 27 : # @invitation.user
Query(User)
.where("id = ?")
# Q 28 : # @invitation.memo.present?
Query(Invitation)
.select('memo')
# Q 29 : # @invitation.memo
Query(Invitation)
.select('memo')
# Q 30 : # @invitation.memo
Query(Invitation)
.select('memo')
# Q 31 : # story.vote
Query(Story)

# Q 32 : # story.vote
Query(Story)

# Q 33 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 34 : # story.score
Query(Story)

# Q 35 : # User.make!(:username => nil)
Query(User)

# Q 36 : # User.make!
Query(User)

# Q 37 : # User.make!(:username => nil)
Query(User)

# Q 38 : # User.make!
Query(User)

# Q 39 : # User.make!(:username => nil)
Query(User)

# Q 40 : # User.make!(:username => nil)
Query(User)

# Q 41 : # User.make!
Query(User)

# Q 42 : # User.make!(:username => nil)
Query(User)

# Q 43 : # User.make!
Query(User)

# Q 44 : # User.make!
Query(User)

# Q 45 : # @user = User.make!
Query(User)

# Q 46 : # @user = User.make!
Query(User)

# Q 47 : # User.make!
Query(User)

# Q 48 : # Story.make!(:title => "hello", :url => "http://example.com/")
Query(Story)

# Q 49 : # Story.make!
Query(Story)

# Q 50 : # Story.make!(:title => "hello", :url => "http://example.com/")
Query(Story)

# Q 51 : # Story.make!
Query(Story)

# Q 52 : # Story.make!(:title => "hello", :url => "http://example.com/")
Query(Story)

# Q 53 : # Story.make!
Query(Story)

# Q 54 : # Story.make!
Query(Story)

# Q 55 : # Comment.make!(:comment => "hello")
Query(Comment)

# Q 56 : # Comment.make!
Query(Comment)

# Q 57 : # Comment.make!(:comment => "hello")
Query(Comment)

# Q 58 : # Comment.make!
Query(Comment)

# Q 59 : # Comment.make!(:comment => "hello")
Query(Comment)

# Q 60 : # Comment.make!
Query(Comment)

# Q 61 : # Comment.make!
Query(Comment)

# Q 62 : # Story.make!
Query(Story)

# Q 63 : # s = Story.make!
Query(Story)

# Q 64 : # s = Story.make!
Query(Story)

# Q 65 : # Story.make!
Query(Story)

# Q 66 : # Message.make!
Query(Message)

# Q 67 : # m = Message.make!
Query(Message)

# Q 68 : # m = Message.make!
Query(Message)

# Q 69 : # Message.make!
Query(Message)

# Q 70 : # if comment.errors.any?
#   
#   
#   errors_for comment
# end
Query(Comment)

# Q 71 : # comment.errors.any?
Query(Comment)

# Q 72 : # comment.errors
Query(Comment)

# Q 73 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 74 : # @comment.url
Query(Comment)

# Q 75 : # @comment.url
Query(Comment)

# Q 76 : # story.score
Query(Story)

# Q 77 : # story.already_posted_story.created_at
Query(Story)
.select('created_at')
# Q 78 : # story.already_posted_story
Query(Story)

# Q 79 : # user.avatar_url(size)
Query(User)

# Q 80 : # user.avatar_url
Query(User)

# Q 81 : # user.avatar_url
Query(User)

# Q 82 : # @user.undeleted_received_messages
Query(User)

# Q 83 : # @user.undeleted_received_messages
Query(User)

# Q 84 : # @user.undeleted_received_messages
Query(User)

# Q 85 : # User.moderators.map(&:username)
Query(User)

# Q 86 : # User.moderators.map
Query(User)

# Q 87 : # User.moderators
Query(User)

# Q 88 : # User.moderators.map
Query(User)

# Q 89 : # User.moderators
Query(User)

# Q 90 : # Search.new
Query(Search)

# Q 91 : # Search.new
Query(Search)

# Q 92 : # Search.new
Query(Search)

# Q 93 : # User.where(:username => params[:username]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 94 : # User.where(:username => params[:username]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 95 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 96 : # User.where(:username => params[:username]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 97 : # Tag.all_with_story_counts_for(nil)
Query(Tag)

# Q 98 : # Tag.all_with_story_counts_for(nil)
Query(Tag)

# Q 99 : # Tag.all_with_story_counts_for
Query(Tag)

# Q 100 : # Tag.all_with_story_counts_for
Query(Tag)

# Q 101 : # User.make!(:username => "")
Query(User)

# Q 102 : # User.make!
Query(User)

# Q 103 : # User.make!(:username => "")
Query(User)

# Q 104 : # User.make!
Query(User)

# Q 105 : # User.make!(:username => "")
Query(User)

# Q 106 : # User.make!(:username => "")
Query(User)

# Q 107 : # User.make!
Query(User)

# Q 108 : # User.make!(:username => "")
Query(User)

# Q 109 : # User.make!
Query(User)

# Q 110 : # Story.make!(:user => @user)
Query(Story)

# Q 111 : # Story.make!
Query(Story)

# Q 112 : # Story.make!(:user => @user)
Query(Story)

# Q 113 : # Story.make!
Query(Story)

# Q 114 : # Story.make!(:user => @user)
Query(Story)

# Q 115 : # Story.make!
Query(Story)

# Q 116 : # Story.make!
Query(Story)

# Q 117 : # comment.persisted?
Query(Comment)

# Q 118 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 119 : # @hat_requests.count
Query(HatRequest)

# Q 120 : # @tags.map { |t|
#   
#   t.stories_count
# }.max
Query(Tag)

# Q 121 : # @tags.map
Query(Tag)

# Q 122 : # @invitation_request.name
Query(InvitationRequest)
.select('name')
# Q 123 : # story.score
Query(Story)

# Q 124 : # @story.short_id
Query(Story)
.select('short_id')
# Q 125 : # @story.short_id
Query(Story)
.select('short_id')
# Q 126 : # where(user_id: user_id).order(comment_created_at: :desc).preload(:comment => [:story, :user])
Query(ReplyingComment)
.where("user_id = ?")
.order('comment_created_at')
.includes('comment')
# Q 127 : # where(user_id: user_id).order(comment_created_at: :desc).preload
Query(ReplyingComment)
.where("user_id = ?")
.order('comment_created_at')
# Q 128 : # where(user_id: user_id).order
Query(ReplyingComment)
.where("user_id = ?")
# Q 129 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 130 : # self.where(:key => key)
Query(Keystore)
.where("key = ?")
# Q 131 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 132 : # user.avatar_url(size)
Query(User)

# Q 133 : # user.avatar_url
Query(User)

# Q 134 : # user.avatar_url(size * 2)
Query(User)

# Q 135 : # user.avatar_url
Query(User)

# Q 136 : # user.avatar_url
Query(User)

# Q 137 : # user.avatar_url
Query(User)

# Q 138 : # @user.stories_submitted_count
Query(User)

# Q 139 : # @user.stories_submitted_count
Query(User)

# Q 140 : # InvitationRequest.new
Query(InvitationRequest)

# Q 141 : # InvitationRequest.new
Query(InvitationRequest)

# Q 142 : # InvitationRequest.new
Query(InvitationRequest)

# Q 143 : # User.make!(:username => "*")
Query(User)

# Q 144 : # User.make!
Query(User)

# Q 145 : # User.make!(:username => "*")
Query(User)

# Q 146 : # User.make!
Query(User)

# Q 147 : # User.make!(:username => "*")
Query(User)

# Q 148 : # User.make!(:username => "*")
Query(User)

# Q 149 : # User.make!
Query(User)

# Q 150 : # User.make!(:username => "*")
Query(User)

# Q 151 : # User.make!
Query(User)

# Q 152 : # comment.current_vote
Query(Comment)

# Q 153 : # comment.current_vote
Query(Comment)

# Q 154 : # @tags.each
Query(Tag)

# Q 155 : # @invitation_request.email
Query(InvitationRequest)
.select('email')
# Q 156 : # @users.each
Query(User)

# Q 157 : # @invitation.code
Query(Invitation)
.select('code')
# Q 158 : # @invitation.code
Query(Invitation)
.select('code')
# Q 159 : # @invitation.code
Query(Invitation)
.select('code')
# Q 160 : # @story.markeddown_description.present?
Query(Story)
.select('markeddown_description')
# Q 161 : # @story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 162 : # story.is_hidden_by_cur_user
Query(Story)

# Q 163 : # story.already_posted_story.comments_path
Query(Story)

# Q 164 : # story.already_posted_story
Query(Story)

# Q 165 : # @user.password_reset_token
Query(User)
.select('password_reset_token')
# Q 166 : # SavedStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize.save!
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 167 : # SavedStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 168 : # SavedStory.where(:user_id => user_id, :story_id => story_id)
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 169 : # SavedStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize.save!
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 170 : # SavedStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 171 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize.save!
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 172 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 173 : # HiddenStory.where(:user_id => user_id, :story_id => story_id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 174 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize.save!
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 175 : # HiddenStory.where(:user_id => user_id, :story_id => story_id).first_or_initialize
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 176 : # Tag.active.all_with_story_counts_for(@user)
Query(Tag)

# Q 177 : # Tag.active.all_with_story_counts_for(@user)
Query(Tag)

# Q 178 : # Tag.active.all_with_story_counts_for
Query(Tag)

# Q 179 : # Tag.active
Query(Tag)

# Q 180 : # Tag.active.all_with_story_counts_for
Query(Tag)

# Q 181 : # Tag.active
Query(Tag)

# Q 182 : # User.make!
Query(User)

# Q 183 : # @commentor = User.make!
Query(User)

# Q 184 : # @commentor = User.make!
Query(User)

# Q 185 : # User.make!
Query(User)

# Q 186 : # tag.stories_count.to_f
Query(Tag)

# Q 187 : # tag.stories_count
Query(Tag)

# Q 188 : # tag.stories_count.to_f
Query(Tag)

# Q 189 : # tag.stories_count
Query(Tag)

# Q 190 : # (
# tag.stories_count.to_f == 0) ? 1 : tag.stories_count.to_f
Query(Tag)

# Q 191 : # tag.stories_count.to_f == 0
Query(Tag)

# Q 192 : # tag.stories_count.to_f
Query(Tag)

# Q 193 : # tag.stories_count
Query(Tag)

# Q 194 : # tag.stories_count.to_f
Query(Tag)

# Q 195 : # tag.stories_count
Query(Tag)

# Q 196 : # @invitation_request.memo
Query(InvitationRequest)
.select('memo')
# Q 197 : # @user.invited_by_user.try
Query(User)
.where("id = ?")
# Q 198 : # @user.invited_by_user
Query(User)
.where("id = ?")
# Q 199 : # @search.q
Query(Search)

# Q 200 : # @search.q
Query(Search)

# Q 201 : # story.is_saved_by_cur_user
Query(Story)

# Q 202 : # where(:inactive => false)
Query(Tag)
.where("inactive = ?")
# Q 203 : # HatRequest.new
Query(HatRequest)

# Q 204 : # HatRequest.new
Query(HatRequest)

# Q 205 : # HatRequest.new
Query(HatRequest)

# Q 206 : # @user.present?
Query(User)

# Q 207 : # @user.dup
Query(User)

# Q 208 : # @user.dup
Query(User)

# Q 209 : # @user.dup
Query(User)

# Q 210 : # ReplyingComment.for_user(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit(REPLIES_PER_PAGE)
Query(ReplyingComment)
.return_limit('')
# Q 211 : # ReplyingComment.for_user(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit(REPLIES_PER_PAGE)
Query(ReplyingComment)
.return_limit('')
# Q 212 : # ReplyingComment.for_user(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit
Query(ReplyingComment)
.return_limit('')
# Q 213 : # ReplyingComment.for_user(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE)
Query(ReplyingComment)

# Q 214 : # ReplyingComment.for_user(@user.id).offset
Query(ReplyingComment)

# Q 215 : # ReplyingComment.for_user(@user.id)
Query(ReplyingComment)

# Q 216 : # ReplyingComment.for_user
Query(ReplyingComment)

# Q 217 : # ReplyingComment.for_user(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit
Query(ReplyingComment)
.return_limit('')
# Q 218 : # ReplyingComment.for_user(@user.id).offset
Query(ReplyingComment)

# Q 219 : # ReplyingComment.for_user
Query(ReplyingComment)

# Q 220 : # User.make!(:username => "test")
Query(User)

# Q 221 : # User.make!
Query(User)

# Q 222 : # User.make!(:username => "test")
Query(User)

# Q 223 : # User.make!(:username => "test")
Query(User)

# Q 224 : # User.make!
Query(User)

# Q 225 : # Comment.make!(:story => @story, :user => @commentor)
Query(Comment)

# Q 226 : # Comment.make!
Query(Comment)

# Q 227 : # Comment.make!(:story => @story, :user => @commentor)
Query(Comment)

# Q 228 : # Comment.make!
Query(Comment)

# Q 229 : # Comment.make!(:story => @story, :user => @commentor)
Query(Comment)

# Q 230 : # Comment.make!
Query(Comment)

# Q 231 : # Comment.make!
Query(Comment)

# Q 232 : # comment.story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 233 : # comment.story
Query(Story)
.where("id = ?")
# Q 234 : # comment.story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 235 : # comment.story
Query(Story)
.where("id = ?")
# Q 236 : # comment.score
Query(Comment)

# Q 237 : # @hat_requests.each_with_index
Query(HatRequest)

# Q 238 : # tag.tag
Query(Tag)
.select('tag')
# Q 239 : # tag.css_class
Query(Tag)

# Q 240 : # tag.tag
Query(Tag)
.select('tag')
# Q 241 : # tag.css_class
Query(Tag)

# Q 242 : # user.username
Query(User)
.select('username')
# Q 243 : # user.username
Query(User)
.select('username')
# Q 244 : # @story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 245 : # story.is_expired?
Query(Story)

# Q 246 : # InvitationRequest.where(:is_verified => true).count
Query(InvitationRequest)
.where("is_verified = ?")
# Q 247 : # InvitationRequest.where(:is_verified => true)
Query(InvitationRequest)
.where("is_verified = ?")
# Q 248 : # InvitationRequest.where(:is_verified => true).count
Query(InvitationRequest)
.where("is_verified = ?")
# Q 249 : # user.username
Query(User)
.select('username')
# Q 250 : # user.username
Query(User)
.select('username')
# Q 251 : # @user.id
Query(User)

# Q 252 : # @user.id
Query(User)

# Q 253 : # User.make!(:username => "test")
Query(User)

# Q 254 : # User.make!
Query(User)

# Q 255 : # User.make!(:username => "test")
Query(User)

# Q 256 : # User.make!
Query(User)

# Q 257 : # User.make!(:username => "test")
Query(User)

# Q 258 : # User.make!(:username => "test")
Query(User)

# Q 259 : # User.make!
Query(User)

# Q 260 : # User.make!(:username => "test")
Query(User)

# Q 261 : # User.make!
Query(User)

# Q 262 : # User.make!(:username => "blahblah")
Query(User)

# Q 263 : # User.make!
Query(User)

# Q 264 : # User.make!(:username => "blahblah")
Query(User)

# Q 265 : # User.make!(:username => "blahblah")
Query(User)

# Q 266 : # User.make!
Query(User)

# Q 267 : # @stories.each
Query(Story)

# Q 268 : # @comments.each
Query(Comment)

# Q 269 : # @user.username
Query(User)
.select('username')
# Q 270 : # user.is_active?
Query(User)

# Q 271 : # user.is_active?
Query(User)

# Q 272 : # for_user(user_id).where(is_unread: true)
Query(ReplyingComment)
.where("is_unread = ?")
# Q 273 : # for_user(user_id).where
Query(ReplyingComment)

# Q 274 : # self.where(:key => key).first.try(:value)
Query(Keystore)
.where("key = ?")
.return_limit('1')
.select('value')
# Q 275 : # self.where(:key => key).first.try
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 276 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 277 : # self.where(:key => key)
Query(Keystore)
.where("key = ?")
# Q 278 : # self.where(:key => key).first.try
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 279 : # self.where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 280 : # Moderation.joins(:story).where("stories.user_id = ? AND moderations.created_at > ?", @user.id, 5.days.ago).exists?
Query(Moderation)
.joins('story')
.where("user_id = ?")
.return_limit('1')
# Q 281 : # Moderation.joins(:story).where("stories.user_id = ? AND moderations.created_at > ?", @user.id, 5.days.ago)
Query(Moderation)
.joins('story')
.where("user_id = ?")
# Q 282 : # Moderation.joins(:story).where
Query(Moderation)
.joins('story')
# Q 283 : # Moderation.joins(:story)
Query(Moderation)
.joins('story')
# Q 284 : # Moderation.joins
Query(Moderation)

# Q 285 : # Moderation.joins(:story).where("stories.user_id = ? AND moderations.created_at > ?", @user.id, 5.days.ago).exists?
Query(Moderation)
.joins('story')
.where("user_id = ?")
.return_limit('1')
# Q 286 : # Moderation.joins(:story).where
Query(Moderation)
.joins('story')
# Q 287 : # Moderation.joins
Query(Moderation)

# Q 288 : # @user.tag_filter_tags.to_a
Query(Tag)
.where("user_id = ?")
# Q 289 : # @user.tag_filter_tags.to_a
Query(Tag)
.where("user_id = ?")
# Q 290 : # @user.tag_filter_tags
Query(Tag)
.where("user_id = ?")
# Q 291 : # @user.tag_filter_tags.to_a
Query(Tag)
.where("user_id = ?")
# Q 292 : # @user.tag_filter_tags
Query(Tag)
.where("user_id = ?")
# Q 293 : # User.make!(:mailing_list_mode => 1)
Query(User)

# Q 294 : # User.make!
Query(User)

# Q 295 : # User.make!(:mailing_list_mode => 1)
Query(User)

# Q 296 : # User.make!
Query(User)

# Q 297 : # User.make!(:mailing_list_mode => 1)
Query(User)

# Q 298 : # User.make!
Query(User)

# Q 299 : # User.make!
Query(User)

# Q 300 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 301 : # Story.make!
Query(Story)

# Q 302 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 303 : # Story.make!
Query(Story)

# Q 304 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 305 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 306 : # Story.make!
Query(Story)

# Q 307 : # Story.make!(:title => "hello", :url => "", :description => "")
Query(Story)

# Q 308 : # Story.make!
Query(Story)

# Q 309 : # User.make!
Query(User)

# Q 310 : # u = User.make!
Query(User)

# Q 311 : # u = User.make!
Query(User)

# Q 312 : # User.make!
Query(User)

# Q 313 : # if comment.parent_comment
#   
#   
#   hidden_field_tag "parent_comment_short_id", comment.parent_comment.short_id
# end
Query(Comment)

# Q 314 : # comment.parent_comment
Query(Comment)
.where("id = ?")
# Q 315 : # comment.id
Query(Comment)

# Q 316 : # comment.id
Query(Comment)

# Q 317 : # comment.id
Query(Comment)

# Q 318 : # comment.id
Query(Comment)

# Q 319 : # @message.subject
Query(Message)
.select('subject')
# Q 320 : # if @user.has_2fa?
#   
#   
# else
#   
#   
# end
Query(User)

# Q 321 : # @user.has_2fa?
Query(User)

# Q 322 : # story.errors.any?
Query(Story)

# Q 323 : # story.errors
Query(Story)

# Q 324 : # if @user.is_moderator?
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
#     f.text_field :moderation_reason
#   end
# end
Query(User)

# Q 325 : # @user.is_moderator?
Query(User)

# Q 326 : # self.tag
Query(Tag)
.select('tag')
# Q 327 : # self.tag
Query(Tag)
.select('tag')
# Q 328 : # Message.new
Query(Message)

# Q 329 : # Message.new
Query(Message)

# Q 330 : # Message.new
Query(Message)

# Q 331 : # Moderation.new
Query(Moderation)

# Q 332 : # Moderation.new
Query(Moderation)

# Q 333 : # Moderation.new
Query(Moderation)

# Q 334 : # self.transaction
Query(HatRequest)

# Q 335 : # self.transaction
Query(HatRequest)

# Q 336 : # @user.id
Query(User)

# Q 337 : # @user.id
Query(User)

# Q 338 : # @user.username
Query(User)
.select('username')
# Q 339 : # @user.username
Query(User)
.select('username')
# Q 340 : # story.title
Query(Story)
.select('title')
# Q 341 : # story.title
Query(Story)
.select('title')
# Q 342 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 343 : # comment.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 344 : # comment.story
Query(Story)
.where("id = ?")
# Q 345 : # comment.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 346 : # comment.story
Query(Story)
.where("id = ?")
# Q 347 : # user.is_new?
Query(User)

# Q 348 : # user.is_new?
Query(User)

# Q 349 : # for_user(user_id).where("parent_comment_id is not null")
Query(ReplyingComment)
.where(" = ?")
# Q 350 : # for_user(user_id).where
Query(ReplyingComment)

# Q 351 : # self.moderator_user_id
Query(Moderation)
.select('moderator_user_id')
# Q 352 : # self.moderator_user_id
Query(Moderation)
.select('moderator_user_id')
# Q 353 : # self.moderator_user_id
Query(Moderation)
.select('moderator_user_id')
# Q 354 : # self.user_id
Query(Hat)
.select('user_id')
# Q 355 : # self.user_id
Query(Hat)
.select('user_id')
# Q 356 : # self.user_id
Query(Hat)
.select('user_id')
# Q 357 : # Hat.new
Query(Hat)

# Q 358 : # Hat.new
Query(Hat)

# Q 359 : # h = Hat.new
Query(Hat)

# Q 360 : # Hat.new
Query(Hat)

# Q 361 : # Message.new
Query(Message)

# Q 362 : # Message.new
Query(Message)

# Q 363 : # @new_message = Message.new
Query(Message)

# Q 364 : # Message.new
Query(Message)

# Q 365 : # @user.try(:authenticate, params[:user][:password].to_s)
Query(User)
.select('authenticate')
# Q 366 : # @user.try
Query(User)

# Q 367 : # @user.try
Query(User)

# Q 368 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 369 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 370 : # Story.where(:short_id => params[:story_id])
Query(Story)
.where("short_id = ?")
# Q 371 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 372 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 373 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 374 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 375 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 376 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 377 : # story.url_or_comments_url
Query(Story)

# Q 378 : # story.url_or_comments_url
Query(Story)

# Q 379 : # comment.parent_comment.short_id
Query(Comment)
.where("id = ?")
.select('short_id')
# Q 380 : # comment.parent_comment
Query(Comment)
.where("id = ?")
# Q 381 : # comment.parent_comment.short_id
Query(Comment)
.where("id = ?")
.select('short_id')
# Q 382 : # comment.parent_comment
Query(Comment)
.where("id = ?")
# Q 383 : # comment.url
Query(Comment)

# Q 384 : # comment.url
Query(Comment)

# Q 385 : # @invitation_request.code
Query(InvitationRequest)
.select('code')
# Q 386 : # @story.is_unavailable
Query(Story)

# Q 387 : # @story.story_cache.present?
Query(Story)
.select('story_cache')
# Q 388 : # @story.story_cache
Query(Story)
.select('story_cache')
# Q 389 : # story.errors.any?
Query(Story)

# Q 390 : # story.errors
Query(Story)

# Q 391 : # story.already_posted_story
Query(Story)

# Q 392 : # for_user(user_id).where("parent_comment_id is null")
Query(ReplyingComment)
.where(" = ?")
# Q 393 : # for_user(user_id).where
Query(ReplyingComment)

# Q 394 : # user.id
Query(User)

# Q 395 : # user.id
Query(User)

# Q 396 : # user.id
Query(User)

# Q 397 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 398 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 399 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 400 : # @user.delete!
Query(User)

# Q 401 : # @user.delete!
Query(User)

# Q 402 : # story.is_gone?
Query(Story)

# Q 403 : # story.is_gone?
Query(Story)

# Q 404 : # User.make!(:email => "user@example.com")
Query(User)

# Q 405 : # User.make!
Query(User)

# Q 406 : # User.make!(:email => "user@example.com")
Query(User)

# Q 407 : # User.make!(:email => "user@example.com")
Query(User)

# Q 408 : # User.make!
Query(User)

# Q 409 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 410 : # Story.make!
Query(Story)

# Q 411 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 412 : # Story.make!
Query(Story)

# Q 413 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 414 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 415 : # Story.make!
Query(Story)

# Q 416 : # Story.make!(:title => "hello", :description => "hi", :url => nil)
Query(Story)

# Q 417 : # Story.make!
Query(Story)

# Q 418 : # story.short_id_url
Query(Story)

# Q 419 : # story.short_id_url
Query(Story)

# Q 420 : # comment.short_id_url
Query(Comment)

# Q 421 : # comment.short_id_url
Query(Comment)

# Q 422 : # self.hat
Query(Hat)
.select('hat')
# Q 423 : # self.hat
Query(Hat)
.select('hat')
# Q 424 : # user.id
Query(User)

# Q 425 : # user.id
Query(User)

# Q 426 : # user.id
Query(User)

# Q 427 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 428 : # Keystore.connection
Query(Keystore)

# Q 429 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 430 : # Keystore.connection
Query(Keystore)

# Q 431 : # Story.new(story_params)
Query(Story)

# Q 432 : # Story.new(story_params)
Query(Story)

# Q 433 : # Story.new
Query(Story)

# Q 434 : # Story.new
Query(Story)

# Q 435 : # @user.can_see_invitation_requests?
Query(User)

# Q 436 : # @user.can_see_invitation_requests?
Query(User)

# Q 437 : # story.url.to_s.match(/\.pdf$/i)
Query(Story)
.select('url')
# Q 438 : # story.url.to_s.match
Query(Story)
.select('url')
# Q 439 : # story.url.to_s
Query(Story)
.select('url')
# Q 440 : # story.url
Query(Story)
.select('url')
# Q 441 : # story.url.to_s.match
Query(Story)
.select('url')
# Q 442 : # story.url.to_s
Query(Story)
.select('url')
# Q 443 : # story.url
Query(Story)
.select('url')
# Q 444 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 445 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 446 : # story.user
Query(User)
.where("id = ?")
# Q 447 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 448 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 449 : # comment.user
Query(User)
.where("id = ?")
# Q 450 : # @message.author
Query(User)
.where("id = ?")
# Q 451 : # user.username
Query(User)
.select('username')
# Q 452 : # user.username
Query(User)
.select('username')
# Q 453 : # @story.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 454 : # TagFilter.group(:tag_id).count
Query(TagFilter)
.group('tag_id')
# Q 455 : # TagFilter.group(:tag_id).count
Query(TagFilter)
.group('tag_id')
# Q 456 : # TagFilter.group(:tag_id)
Query(TagFilter)
.group('tag_id')
# Q 457 : # TagFilter.group
Query(TagFilter)
.group('')
# Q 458 : # TagFilter.group(:tag_id).count
Query(TagFilter)
.group('tag_id')
# Q 459 : # TagFilter.group
Query(TagFilter)
.group('')
# Q 460 : # self.assign_short_id_and_upvote
Query(Comment)

# Q 461 : # self.assign_short_id_and_upvote
Query(Comment)

# Q 462 : # where(:has_been_read => false, :deleted_by_recipient => false)
Query(Message)
.where("has_been_read = ?")
.where("deleted_by_recipient = ?")
# Q 463 : # self.hat
Query(HatRequest)
.select('hat')
# Q 464 : # self.hat
Query(HatRequest)
.select('hat')
# Q 465 : # self.hat
Query(HatRequest)
.select('hat')
# Q 466 : # Keystore.connection.execute
Query(Keystore)

# Q 467 : # Keystore.connection
Query(Keystore)

# Q 468 : # Keystore.connection.execute
Query(Keystore)

# Q 469 : # Keystore.connection
Query(Keystore)

# Q 470 : # @user.id
Query(User)

# Q 471 : # @user.id
Query(User)

# Q 472 : # @user.id
Query(User)

# Q 473 : # Moderation.all.eager_load(:moderator, :story, :comment, :user)
Query(Moderation)
.includes('moderator')
.includes('story')
.includes('comment')
.includes('user')
# Q 474 : # Moderation.all.eager_load(:moderator, :story, :comment, :user)
Query(Moderation)
.includes('moderator')
.includes('story')
.includes('comment')
.includes('user')
# Q 475 : # Moderation.all.eager_load
Query(Moderation)

# Q 476 : # Moderation.all
Query(Moderation)

# Q 477 : # Moderation.all.eager_load
Query(Moderation)

# Q 478 : # Moderation.all
Query(Moderation)

# Q 479 : # @user.disown_comments!
Query(User)

# Q 480 : # @user.disown_comments!
Query(User)

# Q 481 : # story.created_at.rfc2822
Query(Story)
.select('created_at')
# Q 482 : # story.created_at.rfc2822
Query(Story)
.select('created_at')
# Q 483 : # story.created_at
Query(Story)
.select('created_at')
# Q 484 : # comment.is_gone?
Query(Comment)

# Q 485 : # comment.created_at.rfc2822
Query(Comment)
.select('created_at')
# Q 486 : # comment.created_at.rfc2822
Query(Comment)
.select('created_at')
# Q 487 : # comment.created_at
Query(Comment)
.select('created_at')
# Q 488 : # @comments.any?
Query(Comment)

# Q 489 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 490 : # @message.author
Query(User)
.where("id = ?")
# Q 491 : # if user.is_admin?
#   
#   
# elsif user.is_moderator?
#   
#   
# else
#   
#   
#   user.karma
# end
Query(User)

# Q 492 : # user.is_admin?
Query(User)

# Q 493 : # @search.what
Query(Search)

# Q 494 : # @story.short_id
Query(Story)
.select('short_id')
# Q 495 : # story.already_posted_story.created_at
Query(Story)
.select('created_at')
# Q 496 : # story.already_posted_story
Query(Story)

# Q 497 : # self.assign_initial_confidence
Query(Comment)

# Q 498 : # self.assign_initial_confidence
Query(Comment)

# Q 499 : # self.link
Query(HatRequest)
.select('link')
# Q 500 : # self.link
Query(HatRequest)
.select('link')
# Q 501 : # self.link
Query(HatRequest)
.select('link')
# Q 502 : # Keystore.table_name
Query(Keystore)

# Q 503 : # Keystore.table_name
Query(Keystore)

# Q 504 : # Hat.all.includes(:user).each
Query(Hat)
.includes('user')
# Q 505 : # Hat.all.includes(:user)
Query(Hat)
.includes('user')
# Q 506 : # Hat.all.includes
Query(Hat)

# Q 507 : # Hat.all
Query(Hat)

# Q 508 : # Hat.all.includes(:user).each
Query(Hat)
.includes('user')
# Q 509 : # Hat.all.includes
Query(Hat)

# Q 510 : # Hat.all
Query(Hat)

# Q 511 : # User.make!(:email => "user@example.com")
Query(User)

# Q 512 : # User.make!
Query(User)

# Q 513 : # User.make!(:email => "user@example.com")
Query(User)

# Q 514 : # User.make!
Query(User)

# Q 515 : # User.make!(:email => "user@example.com")
Query(User)

# Q 516 : # User.make!(:email => "user@example.com")
Query(User)

# Q 517 : # User.make!
Query(User)

# Q 518 : # User.make!(:email => "user@example.com")
Query(User)

# Q 519 : # User.make!
Query(User)

# Q 520 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 521 : # Story.make!
Query(Story)

# Q 522 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 523 : # Story.make!
Query(Story)

# Q 524 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 525 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 526 : # Story.make!
Query(Story)

# Q 527 : # Story.make!(:title => "hello", :url => "http://ex.com/", :description => nil)
Query(Story)

# Q 528 : # Story.make!
Query(Story)

# Q 529 : # story.comments_url
Query(Story)

# Q 530 : # story.comments_url
Query(Story)

# Q 531 : # comment.comment
Query(Comment)
.select('comment')
# Q 532 : # comment.comment
Query(Comment)
.select('comment')
# Q 533 : # @user.can_downvote?
Query(User)

# Q 534 : # comment.url
Query(Comment)

# Q 535 : # comment.url
Query(Comment)

# Q 536 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 537 : # @message.author
Query(User)
.where("id = ?")
# Q 538 : # story.score
Query(Story)

# Q 539 : # CandidateId.new(klass)
Query(CandidateId)

# Q 540 : # CandidateId.new
Query(CandidateId)

# Q 541 : # CandidateId.new
Query(CandidateId)

# Q 542 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 543 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 544 : # Tag.active.order(:tag)
Query(Tag)
.order('tag')
# Q 545 : # Tag.active.order
Query(Tag)

# Q 546 : # Tag.active
Query(Tag)

# Q 547 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 548 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 549 : # Tag.active.order
Query(Tag)

# Q 550 : # Tag.active
Query(Tag)

# Q 551 : # self.assign_thread_id
Query(Comment)

# Q 552 : # self.assign_thread_id
Query(Comment)

# Q 553 : # self.story
Query(Story)
.where("id = ?")
# Q 554 : # self.story
Query(Story)
.where("id = ?")
# Q 555 : # @story.valid?
Query(Story)

# Q 556 : # @story.already_posted_story
Query(Story)

# Q 557 : # @story.seen_previous
Query(Story)

# Q 558 : # @story.valid?
Query(Story)

# Q 559 : # @story.already_posted_story
Query(Story)

# Q 560 : # @story.seen_previous
Query(Story)

# Q 561 : # User.last.id
Query(User)
.return_limit('1')
# Q 562 : # User.last.id
Query(User)
.return_limit('1')
# Q 563 : # User.last
Query(User)
.return_limit('1')
# Q 564 : # User.last.id
Query(User)
.return_limit('1')
# Q 565 : # User.last
Query(User)
.return_limit('1')
# Q 566 : # story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 567 : # story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 568 : # story.comments
Query(Comment)
.where("story_id = ?")
# Q 569 : # story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 570 : # story.comments
Query(Comment)
.where("story_id = ?")
# Q 571 : # comment.score_for_user
Query(Comment)

# Q 572 : # comment.markeddown_comment
Query(Comment)
.select('markeddown_comment')
# Q 573 : # comment.markeddown_comment
Query(Comment)
.select('markeddown_comment')
# Q 574 : # @message.author.is_admin?
Query(User)
.where("id = ?")
# Q 575 : # @message.author
Query(User)
.where("id = ?")
# Q 576 : # user.is_moderator?
Query(User)

# Q 577 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 578 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 579 : # self.story
Query(Story)
.where("id = ?")
# Q 580 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 581 : # self.story
Query(Story)
.where("id = ?")
# Q 582 : # self.save!
Query(Hat)

# Q 583 : # self.save!
Query(Hat)

# Q 584 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 585 : # Keystore.connection
Query(Keystore)

# Q 586 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 587 : # Keystore.connection
Query(Keystore)

# Q 588 : # @story.save
Query(Story)

# Q 589 : # @story.save
Query(Story)

# Q 590 : # ReplyingComment.comment_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit(REPLIES_PER_PAGE)
Query(ReplyingComment)
.return_limit('')
# Q 591 : # ReplyingComment.comment_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit(REPLIES_PER_PAGE)
Query(ReplyingComment)
.return_limit('')
# Q 592 : # ReplyingComment.comment_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit
Query(ReplyingComment)
.return_limit('')
# Q 593 : # ReplyingComment.comment_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE)
Query(ReplyingComment)

# Q 594 : # ReplyingComment.comment_replies_for(@user.id).offset
Query(ReplyingComment)

# Q 595 : # ReplyingComment.comment_replies_for(@user.id)
Query(ReplyingComment)

# Q 596 : # ReplyingComment.comment_replies_for
Query(ReplyingComment)

# Q 597 : # ReplyingComment.comment_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit
Query(ReplyingComment)
.return_limit('')
# Q 598 : # ReplyingComment.comment_replies_for(@user.id).offset
Query(ReplyingComment)

# Q 599 : # ReplyingComment.comment_replies_for
Query(ReplyingComment)

# Q 600 : # User.where(:session_token => session[:u].to_s).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 601 : # User.where(:session_token => session[:u].to_s).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 602 : # User.where(:session_token => session[:u].to_s)
Query(User)
.where("session_token = ?")
# Q 603 : # User.where(:session_token => session[:u].to_s).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 604 : # story.url
Query(Story)
.select('url')
# Q 605 : # story.url
Query(Story)
.select('url')
# Q 606 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 607 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 608 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 609 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 610 : # @comment.short_id
Query(Comment)
.select('short_id')
# Q 611 : # story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 612 : # story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 613 : # story.already_posted_story.comments_path
Query(Story)

# Q 614 : # story.already_posted_story
Query(Story)

# Q 615 : # InvitationRequest.exists?(:code => self.code)
Query(InvitationRequest)
.return_limit('1')
# Q 616 : # InvitationRequest.exists?
Query(InvitationRequest)
.return_limit('1')
# Q 617 : # self.code
Query(InvitationRequest)
.select('code')
# Q 618 : # InvitationRequest.exists?(:code => self.code)
Query(InvitationRequest)
.return_limit('1')
# Q 619 : # InvitationRequest.exists?
Query(InvitationRequest)
.return_limit('1')
# Q 620 : # self.code
Query(InvitationRequest)
.select('code')
# Q 621 : # InvitationRequest.exists?
Query(InvitationRequest)
.return_limit('1')
# Q 622 : # self.code
Query(InvitationRequest)
.select('code')
# Q 623 : # Invitation.exists?(:code => self.code)
Query(Invitation)
.return_limit('1')
# Q 624 : # Invitation.exists?
Query(Invitation)
.return_limit('1')
# Q 625 : # self.code
Query(Invitation)
.select('code')
# Q 626 : # Invitation.exists?(:code => self.code)
Query(Invitation)
.return_limit('1')
# Q 627 : # Invitation.exists?
Query(Invitation)
.return_limit('1')
# Q 628 : # self.code
Query(Invitation)
.select('code')
# Q 629 : # Invitation.exists?
Query(Invitation)
.return_limit('1')
# Q 630 : # self.code
Query(Invitation)
.select('code')
# Q 631 : # Message.new
Query(Message)

# Q 632 : # Message.new
Query(Message)

# Q 633 : # m = Message.new
Query(Message)

# Q 634 : # Message.new
Query(Message)

# Q 635 : # Keystore.connection.execute
Query(Keystore)

# Q 636 : # Keystore.connection
Query(Keystore)

# Q 637 : # Keystore.table_name
Query(Keystore)

# Q 638 : # Keystore.connection.execute
Query(Keystore)

# Q 639 : # Keystore.connection
Query(Keystore)

# Q 640 : # Keystore.table_name
Query(Keystore)

# Q 641 : # Tag.active.where(:tag => tags_param).to_a
Query(Tag)
.where("tag = ?")
# Q 642 : # Tag.active.where(:tag => tags_param)
Query(Tag)
.where("tag = ?")
# Q 643 : # Tag.active.where
Query(Tag)

# Q 644 : # Tag.active
Query(Tag)

# Q 645 : # Tag.active.where(:tag => tags_param).to_a
Query(Tag)
.where("tag = ?")
# Q 646 : # Tag.active.where
Query(Tag)

# Q 647 : # Tag.active
Query(Tag)

# Q 648 : # ReadRibbon.where(user: @user, story: @story).first_or_create
Query(ReadRibbon)
.where("user = ?")
.where("story = ?")
# Q 649 : # ReadRibbon.where(user: @user, story: @story)
Query(ReadRibbon)
.where("user = ?")
.where("story = ?")
# Q 650 : # ReadRibbon.where(user: @user, story: @story).first_or_create
Query(ReadRibbon)
.where("user = ?")
.where("story = ?")
# Q 651 : # InvitationRequest.where(:is_verified => true)
Query(InvitationRequest)
.where("is_verified = ?")
# Q 652 : # InvitationRequest.where(:is_verified => true)
Query(InvitationRequest)
.where("is_verified = ?")
# Q 653 : # @user.id
Query(User)

# Q 654 : # @user.id
Query(User)

# Q 655 : # user.is_active?
Query(User)

# Q 656 : # user.is_active?
Query(User)

# Q 657 : # User.make!(:email => "user@")
Query(User)

# Q 658 : # User.make!
Query(User)

# Q 659 : # User.make!(:email => "user@")
Query(User)

# Q 660 : # User.make!
Query(User)

# Q 661 : # User.make!(:email => "user@")
Query(User)

# Q 662 : # User.make!(:email => "user@")
Query(User)

# Q 663 : # User.make!
Query(User)

# Q 664 : # User.make!(:email => "user@")
Query(User)

# Q 665 : # User.make!
Query(User)

# Q 666 : # if story.url.present?
#   
#   
#   raw coder.encode("<p>" + link_to("Comments", story.comments_url) + "</p>", :decimal)
# end
Query(Story)

# Q 667 : # story.url.present?
Query(Story)
.select('url')
# Q 668 : # story.url
Query(Story)
.select('url')
# Q 669 : # @message.author.is_moderator?
Query(User)
.where("id = ?")
# Q 670 : # @message.author
Query(User)
.where("id = ?")
# Q 671 : # self.is_from_suggestions?
Query(Moderation)

# Q 672 : # self.is_from_suggestions?
Query(Moderation)

# Q 673 : # user.id
Query(User)

# Q 674 : # user.id
Query(User)

# Q 675 : # user.id
Query(User)

# Q 676 : # where(:merged_story_id => nil)
Query(Story)
.where("merged_story_id = ?")
# Q 677 : # Story.arel_table
Query(Story)

# Q 678 : # Story.arel_table
Query(Story)

# Q 679 : # @story.comments_path
Query(Story)

# Q 680 : # @story.comments_path
Query(Story)

# Q 681 : # @search.valid?
Query(Search)

# Q 682 : # @search.valid?
Query(Search)

# Q 683 : # User.username_regex_s
Query(User)

# Q 684 : # User.username_regex_s
Query(User)

# Q 685 : # @invitation_requests.each
Query(InvitationRequest)

# Q 686 : # user.karma
Query(User)
.select('karma')
# Q 687 : # user.karma
Query(User)
.select('karma')
# Q 688 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 689 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 690 : # @invitation.user
Query(User)
.where("id = ?")
# Q 691 : # @search.what
Query(Search)

# Q 692 : # story.can_be_seen_by_user?
Query(Story)

# Q 693 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 694 : # self.story
Query(Story)
.where("id = ?")
# Q 695 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 696 : # self.story
Query(Story)
.where("id = ?")
# Q 697 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 698 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 699 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 700 : # @search.search_for_user!(@user)
Query(Search)

# Q 701 : # @search.search_for_user!
Query(Search)

# Q 702 : # @search.search_for_user!
Query(Search)

# Q 703 : # @user.wearable_hats.where(:id => params[:hat_id])
Query(Hat)
.where("user_id = ?")
.where("id = ?")
# Q 704 : # @user.wearable_hats.where
Query(Hat)
.where("user_id = ?")
# Q 705 : # @user.wearable_hats
Query(Hat)
.where("user_id = ?")
# Q 706 : # @user.wearable_hats.where
Query(Hat)
.where("user_id = ?")
# Q 707 : # @user.wearable_hats
Query(Hat)
.where("user_id = ?")
# Q 708 : # @user.id
Query(User)

# Q 709 : # @user.username
Query(User)
.select('username')
# Q 710 : # @user.id
Query(User)

# Q 711 : # @user.username
Query(User)
.select('username')
# Q 712 : # Story.make!(:title => "")
Query(Story)

# Q 713 : # Story.make!
Query(Story)

# Q 714 : # Story.make!(:title => "")
Query(Story)

# Q 715 : # Story.make!
Query(Story)

# Q 716 : # Story.make!(:title => "")
Query(Story)

# Q 717 : # Story.make!(:title => "")
Query(Story)

# Q 718 : # Story.make!
Query(Story)

# Q 719 : # Story.make!(:title => "")
Query(Story)

# Q 720 : # Story.make!
Query(Story)

# Q 721 : # story.comments_url
Query(Story)

# Q 722 : # story.comments_url
Query(Story)

# Q 723 : # user.invited_by_user_id
Query(User)
.select('invited_by_user_id')
# Q 724 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 725 : # @invitation.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 726 : # @invitation.user
Query(User)
.where("id = ?")
# Q 727 : # story.url_or_comments_path
Query(Story)

# Q 728 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 729 : # self.story
Query(Story)
.where("id = ?")
# Q 730 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 731 : # self.story
Query(Story)
.where("id = ?")
# Q 732 : # Moderation.new
Query(Moderation)

# Q 733 : # Moderation.new
Query(Moderation)

# Q 734 : # Moderation.new
Query(Moderation)

# Q 735 : # self.hat
Query(HatRequest)
.select('hat')
# Q 736 : # self.hat
Query(HatRequest)
.select('hat')
# Q 737 : # self.hat
Query(HatRequest)
.select('hat')
# Q 738 : # self.hat
Query(HatRequest)
.select('hat')
# Q 739 : # @moderations.where("is_from_suggestions = true")
Query(Moderation)
.where(" = ?")
# Q 740 : # User.order("karma DESC, id ASC").to_a
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 741 : # User.order("karma DESC, id ASC").to_a
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 742 : # User.order("karma DESC, id ASC")
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 743 : # User.order
Query(User)

# Q 744 : # User.order("karma DESC, id ASC").to_a
Query(User)
.order('id')
.order('karma')
.order('id')
# Q 745 : # User.order
Query(User)

# Q 746 : # Story.make!(:title => "hi")
Query(Story)

# Q 747 : # Story.make!
Query(Story)

# Q 748 : # Story.make!(:title => "hi")
Query(Story)

# Q 749 : # Story.make!
Query(Story)

# Q 750 : # Story.make!(:title => "hi")
Query(Story)

# Q 751 : # Story.make!(:title => "hi")
Query(Story)

# Q 752 : # Story.make!
Query(Story)

# Q 753 : # Story.make!(:title => "hi")
Query(Story)

# Q 754 : # Story.make!
Query(Story)

# Q 755 : # Story.make!
Query(Story)

# Q 756 : # s = Story.make!
Query(Story)

# Q 757 : # s = Story.make!
Query(Story)

# Q 758 : # Story.make!
Query(Story)

# Q 759 : # user.username
Query(User)
.select('username')
# Q 760 : # user.username
Query(User)
.select('username')
# Q 761 : # story.title
Query(Story)
.select('title')
# Q 762 : # self.user_id
Query(Hat)
.select('user_id')
# Q 763 : # self.user_id
Query(Hat)
.select('user_id')
# Q 764 : # self.user_id
Query(Hat)
.select('user_id')
# Q 765 : # self.find_or_create_key_for_update(key, value)
Query(Keystore)

# Q 766 : # self.find_or_create_key_for_update(key, value)
Query(Keystore)

# Q 767 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 768 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 769 : # HatRequest.new
Query(HatRequest)

# Q 770 : # HatRequest.new
Query(HatRequest)

# Q 771 : # HatRequest.new
Query(HatRequest)

# Q 772 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 773 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 774 : # Invitation.where(:code => params[:invitation_code].to_s)
Query(Invitation)
.where("code = ?")
# Q 775 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 776 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 777 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 778 : # InvitationRequest.where(:code => params[:code].to_s)
Query(InvitationRequest)
.where("code = ?")
# Q 779 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 780 : # @users.length
Query(User)

# Q 781 : # @users.length
Query(User)

# Q 782 : # @users.length
Query(User)

# Q 783 : # User.make!(:password => "hunter2")
Query(User)

# Q 784 : # User.make!
Query(User)

# Q 785 : # User.make!(:password => "hunter2")
Query(User)

# Q 786 : # User.make!
Query(User)

# Q 787 : # User.make!(:password => "hunter2")
Query(User)

# Q 788 : # User.make!
Query(User)

# Q 789 : # User.make!
Query(User)

# Q 790 : # Story.make!(:title => "hello")
Query(Story)

# Q 791 : # Story.make!
Query(Story)

# Q 792 : # Story.make!(:title => "hello")
Query(Story)

# Q 793 : # Story.make!
Query(Story)

# Q 794 : # Story.make!(:title => "hello")
Query(Story)

# Q 795 : # Story.make!(:title => "hello")
Query(Story)

# Q 796 : # Story.make!
Query(Story)

# Q 797 : # Story.make!(:title => "hello")
Query(Story)

# Q 798 : # Story.make!
Query(Story)

# Q 799 : # @message.author_username
Query(Message)

# Q 800 : # @moderations.each
Query(Moderation)

# Q 801 : # user.is_active?
Query(User)

# Q 802 : # @story.story_cache
Query(Story)
.select('story_cache')
# Q 803 : # Tagging.group(:tag_id).count
Query(Tagging)
.group('tag_id')
# Q 804 : # Tagging.group(:tag_id).count
Query(Tagging)
.group('tag_id')
# Q 805 : # Tagging.group(:tag_id)
Query(Tagging)
.group('tag_id')
# Q 806 : # Tagging.group
Query(Tagging)
.group('')
# Q 807 : # Tagging.group(:tag_id).count
Query(Tagging)
.group('tag_id')
# Q 808 : # Tagging.group
Query(Tagging)
.group('')
# Q 809 : # where(:is_deleted => false, :is_moderated => false)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
# Q 810 : # user.id
Query(User)

# Q 811 : # user.id
Query(User)

# Q 812 : # user.id
Query(User)

# Q 813 : # comment.created_at
Query(Comment)
.select('created_at')
# Q 814 : # comment.user_id
Query(Comment)
.select('user_id')
# Q 815 : # @user.id
Query(User)

# Q 816 : # comment.created_at
Query(Comment)
.select('created_at')
# Q 817 : # comment.user_id
Query(Comment)
.select('user_id')
# Q 818 : # @user.id
Query(User)

# Q 819 : # @user.id
Query(User)

# Q 820 : # @user.id
Query(User)

# Q 821 : # @user.id
Query(User)

# Q 822 : # @moderations.joins(:moderator).where(:users => { :username => @moderator })
Query(Moderation)
.joins('moderator')
.where("username = ?")
# Q 823 : # @moderations.joins(:moderator).where
Query(Moderation)
.joins('moderator')
# Q 824 : # @moderations.joins(:moderator)
Query(Moderation)
.joins('moderator')
# Q 825 : # @moderations.joins
Query(Moderation)

# Q 826 : # @moderations.joins(:moderator).where
Query(Moderation)
.joins('moderator')
# Q 827 : # @moderations.joins
Query(Moderation)

# Q 828 : # User.make!
Query(User)

# Q 829 : # u = User.make!
Query(User)

# Q 830 : # u = User.make!
Query(User)

# Q 831 : # User.make!
Query(User)

# Q 832 : # story.taggings.each do |tagging|
#   
#   
#   tagging.tag.tag
# end
Query(Tagging)
.where("story_id = ?")
# Q 833 : # story.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 834 : # story.taggings
Query(Tagging)
.where("story_id = ?")
# Q 835 : # @messages.any?
Query(Message)

# Q 836 : # if @user.is_moderator?
#   
#   
#   ir.email
# end
Query(User)

# Q 837 : # @user.is_moderator?
Query(User)

# Q 838 : # story.is_gone?
Query(Story)

# Q 839 : # self.action
Query(Moderation)
.select('action')
# Q 840 : # self.action
Query(Moderation)
.select('action')
# Q 841 : # self.hat
Query(Hat)
.select('hat')
# Q 842 : # self.hat
Query(Hat)
.select('hat')
# Q 843 : # User.where(:email => params[:email]).first
Query(User)
.where("email = ?")
.return_limit('1')
# Q 844 : # User.where(:email => params[:email]).first
Query(User)
.where("email = ?")
.return_limit('1')
# Q 845 : # User.where(:email => params[:email])
Query(User)
.where("email = ?")
# Q 846 : # User.where(:email => params[:email]).first
Query(User)
.where("email = ?")
.return_limit('1')
# Q 847 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 848 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 849 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 850 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 851 : # if @user.has_2fa?
#   
#   
#   submit_tag "Disable Two-Factor Authentication"
# else
#   
#   
#   submit_tag "Continue"
# end
Query(User)

# Q 852 : # @user.has_2fa?
Query(User)

# Q 853 : # user.is_new?
Query(User)

# Q 854 : # story.is_moderated?
Query(Story)

# Q 855 : # self.memo
Query(InvitationRequest)
.select('memo')
# Q 856 : # self.memo
Query(InvitationRequest)
.select('memo')
# Q 857 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 858 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 859 : # Tag.active.order(:tag)
Query(Tag)
.order('tag')
# Q 860 : # Tag.active.order
Query(Tag)

# Q 861 : # Tag.active
Query(Tag)

# Q 862 : # Tag.active.order(:tag).select { |t|
#   
#   t.valid_for?(user)
# }.map
Query(Tag)
.order('tag')
# Q 863 : # Tag.active.order(:tag).select
Query(Tag)
.order('tag')
# Q 864 : # Tag.active.order
Query(Tag)

# Q 865 : # Tag.active
Query(Tag)

# Q 866 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id]).first
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 867 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id]).first
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 868 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id])
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
# Q 869 : # story.id
Query(Story)

# Q 870 : # Comment.where(:story_id => story.id, :short_id => params[:parent_comment_short_id]).first
Query(Comment)
.where("story_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 871 : # story.id
Query(Story)

# Q 872 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 873 : # @message.recipient
Query(User)
.where("id = ?")
# Q 874 : # @tags.each do |tag|
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

# Q 875 : # @tags.each
Query(Tag)

# Q 876 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 877 : # self.reason
Query(Moderation)
.select('reason')
# Q 878 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 879 : # self.reason
Query(Moderation)
.select('reason')
# Q 880 : # self.destroy
Query(HatRequest)

# Q 881 : # self.destroy
Query(HatRequest)

# Q 882 : # self.destroy
Query(HatRequest)

# Q 883 : # Vote.where(:user_id => user, :story_id => stories, :comment_id => nil).each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 884 : # Vote.where(:user_id => user, :story_id => stories, :comment_id => nil)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 885 : # Vote.where(:user_id => user, :story_id => stories, :comment_id => nil).each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 886 : # User.where(:username => params[:email]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 887 : # User.where(:username => params[:email]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 888 : # User.where(:username => params[:email])
Query(User)
.where("username = ?")
# Q 889 : # User.where(:username => params[:email]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 890 : # @user.undeleted_sent_messages
Query(User)

# Q 891 : # @user.undeleted_sent_messages
Query(User)

# Q 892 : # @user.undeleted_sent_messages
Query(User)

# Q 893 : # @user.clone
Query(User)

# Q 894 : # @user.clone
Query(User)

# Q 895 : # @user.clone
Query(User)

# Q 896 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 897 : # Story.make!
Query(Story)

# Q 898 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 899 : # Story.make!
Query(Story)

# Q 900 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 901 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 902 : # Story.make!
Query(Story)

# Q 903 : # Story.make!(:title => (
# "hello" * 100))
Query(Story)

# Q 904 : # Story.make!
Query(Story)

# Q 905 : # User.make!(:username => "blahblah")
Query(User)

# Q 906 : # User.make!
Query(User)

# Q 907 : # User.make!(:username => "blahblah")
Query(User)

# Q 908 : # User.make!(:username => "blahblah")
Query(User)

# Q 909 : # User.make!
Query(User)

# Q 910 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 911 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 912 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 913 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 914 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, nil, u.id, nil)
Query(Vote)

# Q 915 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 916 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 917 : # @message.recipient
Query(User)
.where("id = ?")
# Q 918 : # @search.order
Query(Search)

# Q 919 : # @story.user_id
Query(Story)
.select('user_id')
# Q 920 : # @user.id
Query(User)

# Q 921 : # @story.user_id
Query(Story)
.select('user_id')
# Q 922 : # @user.id
Query(User)

# Q 923 : # self.destroy
Query(Hat)

# Q 924 : # self.destroy
Query(Hat)

# Q 925 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 926 : # @story.is_editable_by_user?
Query(Story)

# Q 927 : # @story.is_editable_by_user?
Query(Story)

# Q 928 : # ReplyingComment.story_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit(REPLIES_PER_PAGE)
Query(ReplyingComment)
.return_limit('')
# Q 929 : # ReplyingComment.story_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit(REPLIES_PER_PAGE)
Query(ReplyingComment)
.return_limit('')
# Q 930 : # ReplyingComment.story_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit
Query(ReplyingComment)
.return_limit('')
# Q 931 : # ReplyingComment.story_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE)
Query(ReplyingComment)

# Q 932 : # ReplyingComment.story_replies_for(@user.id).offset
Query(ReplyingComment)

# Q 933 : # ReplyingComment.story_replies_for(@user.id)
Query(ReplyingComment)

# Q 934 : # ReplyingComment.story_replies_for
Query(ReplyingComment)

# Q 935 : # ReplyingComment.story_replies_for(@user.id).offset((
# @page - 1) * REPLIES_PER_PAGE).limit
Query(ReplyingComment)
.return_limit('')
# Q 936 : # ReplyingComment.story_replies_for(@user.id).offset
Query(ReplyingComment)

# Q 937 : # ReplyingComment.story_replies_for
Query(ReplyingComment)

# Q 938 : # @message.created_at
Query(Message)
.select('created_at')
# Q 939 : # tag.tag
Query(Tag)
.select('tag')
# Q 940 : # tag.tag
Query(Tag)
.select('tag')
# Q 941 : # tag.tag
Query(Tag)
.select('tag')
# Q 942 : # @user.id
Query(User)

# Q 943 : # user.username
Query(User)
.select('username')
# Q 944 : # @hat_request.save
Query(HatRequest)

# Q 945 : # @hat_request.save
Query(HatRequest)

# Q 946 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC").to_a
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 947 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC").to_a
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 948 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC")
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 949 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order
Query(User)
.where(" = ?")
# Q 950 : # User.where("is_admin = ? OR is_moderator = ?", true, true)
Query(User)
.where(" = ?")
# Q 951 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order("id ASC").to_a
Query(User)
.where(" = ?")
.order('id')
.order('id')
# Q 952 : # User.where("is_admin = ? OR is_moderator = ?", true, true).order
Query(User)
.where(" = ?")
# Q 953 : # @user.id
Query(User)

# Q 954 : # @user.id
Query(User)

# Q 955 : # user.is_admin?
Query(User)

# Q 956 : # User.username_regex_s
Query(User)

# Q 957 : # User.username_regex_s
Query(User)

# Q 958 : # story.markeddown_description.present?
Query(Story)
.select('markeddown_description')
# Q 959 : # story.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 960 : # User.new
Query(User)

# Q 961 : # User.new
Query(User)

# Q 962 : # User.new
Query(User)

# Q 963 : # @moderations.where("`moderations`.`#{
# type.to_s.singularize}_id` is null")
Query(Moderation)
.where("`#{
type = ?")
# Q 964 : # @moderations.where("`moderations`.`#{
# type.to_s.singularize}_id` is null")
Query(Moderation)
.where("`#{
type = ?")
# Q 965 : # @moderations.where("`moderations`.`#{
# type.to_s.singularize}_id` is null")
Query(Moderation)
.where("`#{
type = ?")
# Q 966 : # @user.authenticate(params[:current_password].to_s)
Query(User)

# Q 967 : # @user.authenticate
Query(User)

# Q 968 : # @user.authenticate
Query(User)

# Q 969 : # tag.tag
Query(Tag)
.select('tag')
# Q 970 : # tag.css_class
Query(Tag)

# Q 971 : # tag.tag
Query(Tag)
.select('tag')
# Q 972 : # tag.css_class
Query(Tag)

# Q 973 : # tag.tag
Query(Tag)
.select('tag')
# Q 974 : # tag.css_class
Query(Tag)

# Q 975 : # story.description
Query(Story)
.select('description')
# Q 976 : # self.reason
Query(Moderation)
.select('reason')
# Q 977 : # self.reason
Query(Moderation)
.select('reason')
# Q 978 : # Vote.votes_by_user_for_stories_hash(@user.id, scope.map(&:id))
Query(Vote)

# Q 979 : # Vote.votes_by_user_for_stories_hash(@user.id, scope.map(&:id))
Query(Vote)

# Q 980 : # Vote.votes_by_user_for_stories_hash
Query(Vote)

# Q 981 : # @user.id
Query(User)

# Q 982 : # Vote.votes_by_user_for_stories_hash
Query(Vote)

# Q 983 : # @user.id
Query(User)

# Q 984 : # @invitation.email
Query(Invitation)
.select('email')
# Q 985 : # @invitation.email
Query(Invitation)
.select('email')
# Q 986 : # @invitation.email
Query(Invitation)
.select('email')
# Q 987 : # @users.length
Query(User)

# Q 988 : # @users.length
Query(User)

# Q 989 : # @users.length
Query(User)

# Q 990 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 991 : # Story.make!
Query(Story)

# Q 992 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 993 : # Story.make!
Query(Story)

# Q 994 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 995 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 996 : # Story.make!
Query(Story)

# Q 997 : # Story.make!(:tags_a => nil)
Query(Story)

# Q 998 : # Story.make!
Query(Story)

# Q 999 : # tag.description
Query(Tag)
.select('description')
# Q 1000 : # tag.description
Query(Tag)
.select('description')
# Q 1001 : # tag.description
Query(Tag)
.select('description')
# Q 1002 : # user.is_moderator?
Query(User)

# Q 1003 : # story.comments_path
Query(Story)

# Q 1004 : # self.link.present?
Query(Hat)
.select('link')
# Q 1005 : # self.link
Query(Hat)
.select('link')
# Q 1006 : # self.link.match(/^https?:\/\//)
Query(Hat)
.select('link')
# Q 1007 : # self.link.match
Query(Hat)
.select('link')
# Q 1008 : # self.link
Query(Hat)
.select('link')
# Q 1009 : # self.link.present?
Query(Hat)
.select('link')
# Q 1010 : # self.link
Query(Hat)
.select('link')
# Q 1011 : # self.link.match
Query(Hat)
.select('link')
# Q 1012 : # self.link
Query(Hat)
.select('link')
# Q 1013 : # self.transaction
Query(HatRequest)

# Q 1014 : # self.transaction
Query(HatRequest)

# Q 1015 : # self.incremented_value_for(key, amount)
Query(Keystore)

# Q 1016 : # self.incremented_value_for
Query(Keystore)

# Q 1017 : # self.incremented_value_for
Query(Keystore)

# Q 1018 : # self.send(p).to_s
Query(Search)

# Q 1019 : # self.send(p)
Query(Search)

# Q 1020 : # self.send
Query(Search)

# Q 1021 : # self.send(p).to_s
Query(Search)

# Q 1022 : # self.send
Query(Search)

# Q 1023 : # User.make!(:username => "admin")
Query(User)

# Q 1024 : # User.make!
Query(User)

# Q 1025 : # User.make!(:username => "admin")
Query(User)

# Q 1026 : # User.make!
Query(User)

# Q 1027 : # User.make!(:username => "admin")
Query(User)

# Q 1028 : # User.make!(:username => "admin")
Query(User)

# Q 1029 : # User.make!
Query(User)

# Q 1030 : # User.make!(:username => "admin")
Query(User)

# Q 1031 : # User.make!
Query(User)

# Q 1032 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 1033 : # Story.make!
Query(Story)

# Q 1034 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 1035 : # Story.make!
Query(Story)

# Q 1036 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 1037 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 1038 : # Story.make!
Query(Story)

# Q 1039 : # Story.make!(:tags_a => ["", " "])
Query(Story)

# Q 1040 : # Story.make!
Query(Story)

# Q 1041 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1042 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1043 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1044 : # @search.order
Query(Search)

# Q 1045 : # self.tag
Query(Tag)
.select('tag')
# Q 1046 : # self.is_media?
Query(Tag)

# Q 1047 : # self.tag
Query(Tag)
.select('tag')
# Q 1048 : # self.is_media?
Query(Tag)

# Q 1049 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map(&:story_id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1050 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map(&:story_id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1051 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1052 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id))
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1053 : # @user.id
Query(User)

# Q 1054 : # HiddenStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1055 : # @user.id
Query(User)

# Q 1056 : # Message.new
Query(Message)

# Q 1057 : # Message.new
Query(Message)

# Q 1058 : # m = Message.new
Query(Message)

# Q 1059 : # Message.new
Query(Message)

# Q 1060 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 1061 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 1062 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token)
Query(User)
.where(" = ?")
# Q 1063 : # User.where("mailing_list_mode > 0 AND mailing_list_token = ?", user_token).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 1064 : # @message.linkified_body
Query(Message)

# Q 1065 : # story.can_be_seen_by_user?
Query(Story)

# Q 1066 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1067 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1068 : # user.id
Query(User)

# Q 1069 : # user.id
Query(User)

# Q 1070 : # user.id
Query(User)

# Q 1071 : # user.id
Query(User)

# Q 1072 : # user.id
Query(User)

# Q 1073 : # @moderations.count
Query(Moderation)

# Q 1074 : # @moderations.count
Query(Moderation)

# Q 1075 : # user.is_active?
Query(User)

# Q 1076 : # user.is_active?
Query(User)

# Q 1077 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1078 : # Story.make!
Query(Story)

# Q 1079 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1080 : # Story.make!
Query(Story)

# Q 1081 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1082 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1083 : # Story.make!
Query(Story)

# Q 1084 : # Story.make!(:tags_a => ["", "tag1"])
Query(Story)

# Q 1085 : # Story.make!
Query(Story)

# Q 1086 : # comment.new_record?
Query(Comment)

# Q 1087 : # comment.new_record? ? "Post" : "Update"
Query(Comment)

# Q 1088 : # comment.new_record?
Query(Comment)

# Q 1089 : # @messages.includes(:author, :recipient).each do |message|
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
# Q 1090 : # @messages.includes(:author, :recipient).each
Query(Message)
.includes('author')
.includes('recipient')
# Q 1091 : # @messages.includes
Query(Message)

# Q 1092 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1093 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1094 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1095 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1096 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1097 : # user.karma
Query(User)
.select('karma')
# Q 1098 : # @story.previewing
Query(Story)

# Q 1099 : # @story.valid?
Query(Story)

# Q 1100 : # self.comment.user_id
Query(Comment)
.where("id = ?")
.select('user_id')
# Q 1101 : # self.comment.user_id
Query(Comment)
.where("id = ?")
.select('user_id')
# Q 1102 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1103 : # self.comment.user_id
Query(Comment)
.where("id = ?")
.select('user_id')
# Q 1104 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1105 : # self.hat.gsub(/[^A-Za-z0-9]/, "_").downcase
Query(Hat)
.select('hat')
# Q 1106 : # self.hat.gsub(/[^A-Za-z0-9]/, "_")
Query(Hat)
.select('hat')
# Q 1107 : # self.hat.gsub
Query(Hat)
.select('hat')
# Q 1108 : # self.hat
Query(Hat)
.select('hat')
# Q 1109 : # self.hat.gsub(/[^A-Za-z0-9]/, "_").downcase
Query(Hat)
.select('hat')
# Q 1110 : # self.hat.gsub
Query(Hat)
.select('hat')
# Q 1111 : # self.hat
Query(Hat)
.select('hat')
# Q 1112 : # SavedStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map(&:story_id)
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1113 : # SavedStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map(&:story_id)
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1114 : # SavedStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1115 : # SavedStory.where(:user_id => @user.id, :story_id => scope.map(&:id))
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1116 : # @user.id
Query(User)

# Q 1117 : # SavedStory.where(:user_id => @user.id, :story_id => scope.map(&:id)).map
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 1118 : # @user.id
Query(User)

# Q 1119 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 1120 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 1121 : # self.user_id
Query(HatRequest)
.select('user_id')
# Q 1122 : # message.has_been_read? ? "" : "bold"
Query(Message)

# Q 1123 : # message.has_been_read? ? "" : "bold"
Query(Message)

# Q 1124 : # message.has_been_read?
Query(Message)

# Q 1125 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1126 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1127 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1128 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1129 : # tag.hotness_mod
Query(Tag)
.select('hotness_mod')
# Q 1130 : # story.sorted_taggings.each
Query(Story)

# Q 1131 : # story.sorted_taggings
Query(Story)

# Q 1132 : # self.granted_by_user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1133 : # self.granted_by_user
Query(User)
.where("id = ?")
# Q 1134 : # self.granted_by_user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1135 : # self.granted_by_user
Query(User)
.where("id = ?")
# Q 1136 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1137 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1138 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1139 : # self.hat
Query(HatRequest)
.select('hat')
# Q 1140 : # Keystore.transaction
Query(Keystore)

# Q 1141 : # Keystore.transaction
Query(Keystore)

# Q 1142 : # self.total_results.to_i
Query(Search)

# Q 1143 : # self.total_results.to_i
Query(Search)

# Q 1144 : # self.total_results
Query(Search)

# Q 1145 : # self.total_results.to_i
Query(Search)

# Q 1146 : # self.total_results
Query(Search)

# Q 1147 : # @story.user_id
Query(Story)
.select('user_id')
# Q 1148 : # @user.id
Query(User)

# Q 1149 : # @story.user_id
Query(Story)
.select('user_id')
# Q 1150 : # @user.id
Query(User)

# Q 1151 : # Message.new
Query(Message)

# Q 1152 : # Message.new
Query(Message)

# Q 1153 : # @new_message = Message.new
Query(Message)

# Q 1154 : # Message.new
Query(Message)

# Q 1155 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id).first
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
.return_limit('1')
# Q 1156 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id).first
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
.return_limit('1')
# Q 1157 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id)
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
# Q 1158 : # story.id
Query(Story)

# Q 1159 : # Comment.where(:story_id => story.id, :user_id => @user.id, :parent_comment_id => comment.parent_comment_id).first
Query(Comment)
.where("story_id = ?")
.where("user_id = ?")
.where("parent_comment_id = ?")
.return_limit('1')
# Q 1160 : # story.id
Query(Story)

# Q 1161 : # message.short_id
Query(Message)
.select('short_id')
# Q 1162 : # message.short_id
Query(Message)
.select('short_id')
# Q 1163 : # message.short_id
Query(Message)
.select('short_id')
# Q 1164 : # message.short_id
Query(Message)
.select('short_id')
# Q 1165 : # message.short_id
Query(Message)
.select('short_id')
# Q 1166 : # user.id
Query(User)

# Q 1167 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1168 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1169 : # self.privileged?
Query(Tag)

# Q 1170 : # self.privileged?
Query(Tag)

# Q 1171 : # self.comment.story.title
Query(Story)
.where("id = ?")
.where("id = ?")
.select('title')
# Q 1172 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1173 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1174 : # self.comment.story.title
Query(Story)
.where("id = ?")
.where("id = ?")
.select('title')
# Q 1175 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1176 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1177 : # self.author.try(:username)
Query(User)
.where("id = ?")
.select('username')
# Q 1178 : # self.author.try(:username)
Query(User)
.where("id = ?")
.select('username')
# Q 1179 : # self.author.try
Query(User)
.where("id = ?")
# Q 1180 : # self.author
Query(User)
.where("id = ?")
# Q 1181 : # self.author.try
Query(User)
.where("id = ?")
# Q 1182 : # self.author
Query(User)
.where("id = ?")
# Q 1183 : # self.created_at.strftime("%Y-%m-%d")
Query(Hat)
.select('created_at')
# Q 1184 : # self.created_at.strftime
Query(Hat)
.select('created_at')
# Q 1185 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1186 : # self.created_at.strftime
Query(Hat)
.select('created_at')
# Q 1187 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1188 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1189 : # Keystore.connection
Query(Keystore)

# Q 1190 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1191 : # Keystore.connection
Query(Keystore)

# Q 1192 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1193 : # Keystore.connection
Query(Keystore)

# Q 1194 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 1195 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 1196 : # Invitation.where(:code => params[:invitation_code].to_s)
Query(Invitation)
.where("code = ?")
# Q 1197 : # Invitation.where(:code => params[:invitation_code].to_s).first
Query(Invitation)
.where("code = ?")
.return_limit('1')
# Q 1198 : # user.authenticate(params[:password].to_s)
Query(User)

# Q 1199 : # user.authenticate
Query(User)

# Q 1200 : # user.authenticate
Query(User)

# Q 1201 : # @user.can_invite?
Query(User)

# Q 1202 : # @user.can_invite?
Query(User)

# Q 1203 : # User.order("id DESC").to_a
Query(User)
.order('id')
.order('id')
# Q 1204 : # User.order("id DESC").to_a
Query(User)
.order('id')
.order('id')
# Q 1205 : # User.order("id DESC")
Query(User)
.order('id')
.order('id')
# Q 1206 : # User.order
Query(User)

# Q 1207 : # User.order("id DESC").to_a
Query(User)
.order('id')
.order('id')
# Q 1208 : # User.order
Query(User)

# Q 1209 : # @user.id
Query(User)

# Q 1210 : # @user.id
Query(User)

# Q 1211 : # User.make!(:banned)
Query(User)

# Q 1212 : # User.make!
Query(User)

# Q 1213 : # User.make!(:banned)
Query(User)

# Q 1214 : # User.make!
Query(User)

# Q 1215 : # User.make!(:banned)
Query(User)

# Q 1216 : # User.make!
Query(User)

# Q 1217 : # User.make!
Query(User)

# Q 1218 : # @search.order
Query(Search)

# Q 1219 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1220 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1221 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1222 : # user.try(:is_moderator?)
Query(User)
.select('is_moderator?')
# Q 1223 : # user.try
Query(User)

# Q 1224 : # user.try
Query(User)

# Q 1225 : # self.comment.story.comments_url
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1226 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1227 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1228 : # self.comment.story.comments_url
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1229 : # self.comment.story
Query(Story)
.where("id = ?")
.where("id = ?")
# Q 1230 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1231 : # self.recipient.try(:username)
Query(User)
.where("id = ?")
.select('username')
# Q 1232 : # self.recipient.try(:username)
Query(User)
.where("id = ?")
.select('username')
# Q 1233 : # self.recipient.try
Query(User)
.where("id = ?")
# Q 1234 : # self.recipient
Query(User)
.where("id = ?")
# Q 1235 : # self.recipient.try
Query(User)
.where("id = ?")
# Q 1236 : # self.recipient
Query(User)
.where("id = ?")
# Q 1237 : # Vote.where(:user_id => user_id, :story_id => story_id).where("comment_id IS NOT NULL").each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where(" = ?")
# Q 1238 : # Vote.where(:user_id => user_id, :story_id => story_id).where("comment_id IS NOT NULL")
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where(" = ?")
# Q 1239 : # Vote.where(:user_id => user_id, :story_id => story_id).where
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
# Q 1240 : # Vote.where(:user_id => user_id, :story_id => story_id)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
# Q 1241 : # Vote.where(:user_id => user_id, :story_id => story_id).where("comment_id IS NOT NULL").each
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where(" = ?")
# Q 1242 : # Vote.where(:user_id => user_id, :story_id => story_id).where
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
# Q 1243 : # Keystore.connection.execute
Query(Keystore)

# Q 1244 : # Keystore.connection
Query(Keystore)

# Q 1245 : # Keystore.connection.execute
Query(Keystore)

# Q 1246 : # Keystore.connection
Query(Keystore)

# Q 1247 : # Keystore.connection.execute
Query(Keystore)

# Q 1248 : # Keystore.connection
Query(Keystore)

# Q 1249 : # self.max_matches
Query(Search)

# Q 1250 : # self.max_matches
Query(Search)

# Q 1251 : # users.length
Query(User)

# Q 1252 : # users.length
Query(User)

# Q 1253 : # users.length
Query(User)

# Q 1254 : # ReplyingComment.unread_replies_for(@user.id)
Query(ReplyingComment)

# Q 1255 : # ReplyingComment.unread_replies_for(@user.id)
Query(ReplyingComment)

# Q 1256 : # ReplyingComment.unread_replies_for
Query(ReplyingComment)

# Q 1257 : # @user.id
Query(User)

# Q 1258 : # ReplyingComment.unread_replies_for
Query(ReplyingComment)

# Q 1259 : # @user.id
Query(User)

# Q 1260 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1261 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1262 : # User.make!
Query(User)

# Q 1263 : # user = User.make!
Query(User)

# Q 1264 : # user = User.make!
Query(User)

# Q 1265 : # User.make!
Query(User)

# Q 1266 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1267 : # Story.make!
Query(Story)

# Q 1268 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1269 : # Story.make!
Query(Story)

# Q 1270 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1271 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1272 : # Story.make!
Query(Story)

# Q 1273 : # Story.make!(:title => "test", :url => "http://gooses.com/")
Query(Story)

# Q 1274 : # Story.make!
Query(Story)

# Q 1275 : # Story.make!
Query(Story)

# Q 1276 : # s = Story.make!
Query(Story)

# Q 1277 : # s = Story.make!
Query(Story)

# Q 1278 : # Story.make!
Query(Story)

# Q 1279 : # message.author
Query(User)
.where("id = ?")
# Q 1280 : # if message.author
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

# Q 1281 : # message.author
Query(User)
.where("id = ?")
# Q 1282 : # if message.author
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

# Q 1283 : # message.author
Query(User)
.where("id = ?")
# Q 1284 : # tag.stories_count
Query(Tag)

# Q 1285 : # tag.stories_count
Query(Tag)

# Q 1286 : # tag.stories_count
Query(Tag)

# Q 1287 : # @story.previewing
Query(Story)

# Q 1288 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1289 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1290 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1291 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1292 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1293 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1294 : # self.link.present?
Query(Hat)
.select('link')
# Q 1295 : # self.link
Query(Hat)
.select('link')
# Q 1296 : # self.link.present?
Query(Hat)
.select('link')
# Q 1297 : # self.link
Query(Hat)
.select('link')
# Q 1298 : # Keystore.table_name
Query(Keystore)

# Q 1299 : # Keystore.table_name
Query(Keystore)

# Q 1300 : # Keystore.table_name
Query(Keystore)

# Q 1301 : # Keystore.table_name
Query(Keystore)

# Q 1302 : # self.max_matches
Query(Search)

# Q 1303 : # self.max_matches
Query(Search)

# Q 1304 : # self.max_matches
Query(Search)

# Q 1305 : # users.group_by(&:invited_by_user_id)
Query(User)

# Q 1306 : # users.group_by(&:invited_by_user_id)
Query(User)

# Q 1307 : # users.group_by
Query(User)

# Q 1308 : # users.group_by
Query(User)

# Q 1309 : # User.where(:username => username).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1310 : # User.where(:username => username).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1311 : # User.where(:username => username)
Query(User)
.where("username = ?")
# Q 1312 : # User.where(:username => username).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1313 : # @user.is_moderator?
Query(User)

# Q 1314 : # @user.is_moderator?
Query(User)

# Q 1315 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 1316 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1317 : # message.author
Query(User)
.where("id = ?")
# Q 1318 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1319 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1320 : # message.author
Query(User)
.where("id = ?")
# Q 1321 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1322 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1323 : # message.author
Query(User)
.where("id = ?")
# Q 1324 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1325 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1326 : # self.comment
Query(Comment)
.select('comment')
# Q 1327 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1328 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1329 : # self.comment
Query(Comment)
.select('comment')
# Q 1330 : # self.comment.comment
Query(Comment)
.where("id = ?")
.select('comment')
# Q 1331 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1332 : # self.comment.comment
Query(Comment)
.where("id = ?")
.select('comment')
# Q 1333 : # self.comment
Query(Comment)
.where("id = ?")
# Q 1334 : # self.link
Query(Hat)
.select('link')
# Q 1335 : # self.link
Query(Hat)
.select('link')
# Q 1336 : # self.destroy
Query(HatRequest)

# Q 1337 : # self.destroy
Query(HatRequest)

# Q 1338 : # self.destroy
Query(HatRequest)

# Q 1339 : # HatRequest.all.includes(:user)
Query(HatRequest)
.includes('user')
# Q 1340 : # HatRequest.all.includes(:user)
Query(HatRequest)
.includes('user')
# Q 1341 : # HatRequest.all.includes
Query(HatRequest)

# Q 1342 : # HatRequest.all
Query(HatRequest)

# Q 1343 : # HatRequest.all.includes
Query(HatRequest)

# Q 1344 : # HatRequest.all
Query(HatRequest)

# Q 1345 : # @story.save(:validate => false)
Query(Story)

# Q 1346 : # @story.save
Query(Story)

# Q 1347 : # @story.save
Query(Story)

# Q 1348 : # User.order("id DESC").limit(10)
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 1349 : # User.order("id DESC").limit(10)
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 1350 : # User.order("id DESC").limit
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 1351 : # User.order("id DESC")
Query(User)
.order('id')
.order('id')
# Q 1352 : # User.order
Query(User)

# Q 1353 : # User.order("id DESC").limit
Query(User)
.order('id')
.order('id')
.return_limit('')
# Q 1354 : # User.order
Query(User)

# Q 1355 : # comment.errors.add(:comment, "^You have already posted a comment " << "here recently.")
Query(Comment)

# Q 1356 : # comment.errors.add
Query(Comment)

# Q 1357 : # comment.errors
Query(Comment)

# Q 1358 : # comment.errors.add
Query(Comment)

# Q 1359 : # comment.errors
Query(Comment)

# Q 1360 : # user.is_banned?
Query(User)

# Q 1361 : # user.is_banned?
Query(User)

# Q 1362 : # user.is_banned?
Query(User)

# Q 1363 : # user.is_banned?
Query(User)

# Q 1364 : # comment.persisted?
Query(Comment)

# Q 1365 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1366 : # comment.persisted?
Query(Comment)

# Q 1367 : # comment.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 1368 : # @message.short_id
Query(Message)
.select('short_id')
# Q 1369 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1370 : # message.author
Query(User)
.where("id = ?")
# Q 1371 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1372 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1373 : # message.author
Query(User)
.where("id = ?")
# Q 1374 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1375 : # message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1376 : # message.author
Query(User)
.where("id = ?")
# Q 1377 : # @story.is_gone?
Query(Story)

# Q 1378 : # @story.previewing
Query(Story)

# Q 1379 : # Keystore.connection.execute
Query(Keystore)

# Q 1380 : # Keystore.connection
Query(Keystore)

# Q 1381 : # Keystore.table_name
Query(Keystore)

# Q 1382 : # Keystore.connection.execute
Query(Keystore)

# Q 1383 : # Keystore.connection
Query(Keystore)

# Q 1384 : # Keystore.table_name
Query(Keystore)

# Q 1385 : # Keystore.table_name
Query(Keystore)

# Q 1386 : # Keystore.connection.execute
Query(Keystore)

# Q 1387 : # Keystore.connection
Query(Keystore)

# Q 1388 : # Keystore.table_name
Query(Keystore)

# Q 1389 : # user.is_banned?
Query(User)

# Q 1390 : # user.is_banned?
Query(User)

# Q 1391 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1392 : # Story.make!
Query(Story)

# Q 1393 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1394 : # Story.make!
Query(Story)

# Q 1395 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1396 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1397 : # Story.make!
Query(Story)

# Q 1398 : # Story.make!(:title => "test", url => "ftp://gooses/")
Query(Story)

# Q 1399 : # Story.make!
Query(Story)

# Q 1400 : # User.make!
Query(User)

# Q 1401 : # u = User.make!
Query(User)

# Q 1402 : # u = User.make!
Query(User)

# Q 1403 : # User.make!
Query(User)

# Q 1404 : # story.domain.present?
Query(Story)

# Q 1405 : # story.domain
Query(Story)

# Q 1406 : # @story.previewing
Query(Story)

# Q 1407 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 1408 : # self.reason
Query(Moderation)
.select('reason')
# Q 1409 : # self.reason.present?
Query(Moderation)
.select('reason')
# Q 1410 : # self.reason
Query(Moderation)
.select('reason')
# Q 1411 : # self.per_page.to_i
Query(Search)

# Q 1412 : # self.per_page
Query(Search)

# Q 1413 : # self.per_page.to_i
Query(Search)

# Q 1414 : # self.per_page
Query(Search)

# Q 1415 : # @story.comments_path
Query(Story)

# Q 1416 : # @story.comments_path
Query(Story)

# Q 1417 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE).order("moderations.created_at desc").limit(ENTRIES_PER_PAGE)
Query(Moderation)
.order('id')
.order('created_at')
.return_limit('')
# Q 1418 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE).order("moderations.created_at desc").limit(ENTRIES_PER_PAGE)
Query(Moderation)
.order('id')
.order('created_at')
.return_limit('')
# Q 1419 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE).order("moderations.created_at desc").limit
Query(Moderation)
.order('id')
.order('created_at')
.return_limit('')
# Q 1420 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE).order("moderations.created_at desc")
Query(Moderation)
.order('id')
.order('created_at')
# Q 1421 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE).order
Query(Moderation)

# Q 1422 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE)
Query(Moderation)

# Q 1423 : # @moderations.offset
Query(Moderation)

# Q 1424 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE).order("moderations.created_at desc").limit
Query(Moderation)
.order('id')
.order('created_at')
.return_limit('')
# Q 1425 : # @moderations.offset((
# @page - 1) * ENTRIES_PER_PAGE).order
Query(Moderation)

# Q 1426 : # @moderations.offset
Query(Moderation)

# Q 1427 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 1428 : # message.author_username
Query(Message)

# Q 1429 : # message.author_username
Query(Message)

# Q 1430 : # message.author_username
Query(Message)

# Q 1431 : # message.author_username
Query(Message)

# Q 1432 : # message.author_username
Query(Message)

# Q 1433 : # @invitation_requests.count
Query(InvitationRequest)

# Q 1434 : # story.domain_search_url
Query(Story)

# Q 1435 : # self.user_id.blank? && errors.add(:user_id, "cannot be blank.")
Query(Comment)

# Q 1436 : # self.user_id.blank?
Query(Comment)
.select('user_id')
# Q 1437 : # self.user_id
Query(Comment)
.select('user_id')
# Q 1438 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1439 : # Keystore.connection
Query(Keystore)

# Q 1440 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1441 : # Keystore.connection
Query(Keystore)

# Q 1442 : # Keystore.connection.adapter_name
Query(Keystore)

# Q 1443 : # Keystore.connection
Query(Keystore)

# Q 1444 : # Invitation.new
Query(Invitation)

# Q 1445 : # Invitation.new
Query(Invitation)

# Q 1446 : # Invitation.new
Query(Invitation)

# Q 1447 : # Keystore.transaction
Query(Keystore)

# Q 1448 : # Keystore.transaction
Query(Keystore)

# Q 1449 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, nil, u.id, "H")
Query(Vote)

# Q 1450 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1451 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, nil, u.id, "H")
Query(Vote)

# Q 1452 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, nil, u.id, "H")
Query(Vote)

# Q 1453 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1454 : # story.domain
Query(Story)

# Q 1455 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 1456 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 1457 : # ShortId.new(self.class)
Query(ShortId)

# Q 1458 : # ShortId.new
Query(ShortId)

# Q 1459 : # self.class
Query(Message)

# Q 1460 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 1461 : # ShortId.new
Query(ShortId)

# Q 1462 : # self.class
Query(Message)

# Q 1463 : # Keystore.connection.execute
Query(Keystore)

# Q 1464 : # Keystore.connection
Query(Keystore)

# Q 1465 : # Keystore.table_name
Query(Keystore)

# Q 1466 : # Keystore.connection.execute
Query(Keystore)

# Q 1467 : # Keystore.connection
Query(Keystore)

# Q 1468 : # Keystore.table_name
Query(Keystore)

# Q 1469 : # Keystore.table_name
Query(Keystore)

# Q 1470 : # Keystore.connection.execute
Query(Keystore)

# Q 1471 : # Keystore.connection
Query(Keystore)

# Q 1472 : # Keystore.table_name
Query(Keystore)

# Q 1473 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1474 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1475 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1476 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1477 : # User.new(user_params)
Query(User)

# Q 1478 : # User.new(user_params)
Query(User)

# Q 1479 : # User.new
Query(User)

# Q 1480 : # User.new
Query(User)

# Q 1481 : # @user.id
Query(User)

# Q 1482 : # @user.id
Query(User)

# Q 1483 : # @user.id
Query(User)

# Q 1484 : # User.make!(:banned)
Query(User)

# Q 1485 : # User.make!
Query(User)

# Q 1486 : # User.make!(:banned)
Query(User)

# Q 1487 : # User.make!
Query(User)

# Q 1488 : # User.make!(:banned)
Query(User)

# Q 1489 : # User.make!
Query(User)

# Q 1490 : # User.make!
Query(User)

# Q 1491 : # @user.is_moderator?
Query(User)

# Q 1492 : # TagFilter.where(:tag_id => self.id).count
Query(TagFilter)
.where("tag_id = ?")
# Q 1493 : # TagFilter.where(:tag_id => self.id)
Query(TagFilter)
.where("tag_id = ?")
# Q 1494 : # self.id
Query(Tag)

# Q 1495 : # TagFilter.where(:tag_id => self.id).count
Query(TagFilter)
.where("tag_id = ?")
# Q 1496 : # self.id
Query(Tag)

# Q 1497 : # @hat_request.update_attributes!(params.require(:hat_request).permit(:hat, :link))
Query(HatRequest)

# Q 1498 : # @hat_request.update_attributes!
Query(HatRequest)

# Q 1499 : # @hat_request.update_attributes!
Query(HatRequest)

# Q 1500 : # @invitation.user_id
Query(Invitation)
.select('user_id')
# Q 1501 : # @invitation.user_id
Query(Invitation)
.select('user_id')
# Q 1502 : # @invitation.user_id
Query(Invitation)
.select('user_id')
# Q 1503 : # user.is_active?
Query(User)

# Q 1504 : # user.is_active?
Query(User)

# Q 1505 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 1506 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 1507 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 1508 : # story.archive_url
Query(Story)

# Q 1509 : # story.archive_url
Query(Story)

# Q 1510 : # User.make!
Query(User)

# Q 1511 : # user = User.make!
Query(User)

# Q 1512 : # user = User.make!
Query(User)

# Q 1513 : # User.make!
Query(User)

# Q 1514 : # comment.short_id
Query(Comment)
.select('short_id')
# Q 1515 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1516 : # message.recipient
Query(User)
.where("id = ?")
# Q 1517 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1518 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1519 : # message.recipient
Query(User)
.where("id = ?")
# Q 1520 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1521 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1522 : # message.recipient
Query(User)
.where("id = ?")
# Q 1523 : # @comments.group_by
Query(Comment)

# Q 1524 : # self.story_id.blank? && errors.add(:story_id, "cannot be blank.")
Query(Comment)

# Q 1525 : # self.story_id.blank?
Query(Comment)
.select('story_id')
# Q 1526 : # self.story_id
Query(Comment)
.select('story_id')
# Q 1527 : # self.reason
Query(Moderation)
.select('reason')
# Q 1528 : # self.reason
Query(Moderation)
.select('reason')
# Q 1529 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC").reject
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1530 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC")
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1531 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1532 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago))
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1533 : # stories.select(:id, :upvotes, :downvotes, :user_id).where
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1534 : # stories.select(:id, :upvotes, :downvotes, :user_id)
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1535 : # stories.select
Query(Story)

# Q 1536 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC").reject
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1537 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC")
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1538 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1539 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago))
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1540 : # stories.select(:id, :upvotes, :downvotes, :user_id).where
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1541 : # stories.select(:id, :upvotes, :downvotes, :user_id)
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1542 : # stories.select
Query(Story)

# Q 1543 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order("stories.created_at DESC").reject
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
.order('id')
.order('created_at')
# Q 1544 : # stories.select(:id, :upvotes, :downvotes, :user_id).where(Story.arel_table[:created_at].gt((
# RECENT_DAYS_OLD + x).days.ago)).order
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1545 : # stories.select(:id, :upvotes, :downvotes, :user_id).where
Query(Story)
.select('id')
.select('upvotes')
.select('downvotes')
.select('user_id')
# Q 1546 : # stories.select
Query(Story)

# Q 1547 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 1548 : # @story.is_editable_by_user?
Query(Story)

# Q 1549 : # @story.is_editable_by_user?
Query(Story)

# Q 1550 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 1551 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 1552 : # Keystore.find_or_create_key_for_update
Query(Keystore)

# Q 1553 : # Comment.where(:short_id => m[1]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 1554 : # Comment.where(:short_id => m[1]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 1555 : # Comment.where(:short_id => m[1])
Query(Comment)
.where("short_id = ?")
# Q 1556 : # Comment.where(:short_id => m[1]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 1557 : # Story.count
Query(Story)

# Q 1558 : # Story.count
Query(Story)

# Q 1559 : # Story.count
Query(Story)

# Q 1560 : # Story.count
Query(Story)

# Q 1561 : # @user.wearable_hats.any?
Query(Hat)
.where("user_id = ?")
# Q 1562 : # @user.wearable_hats
Query(Hat)
.where("user_id = ?")
# Q 1563 : # @user.wearable_hats.any?
Query(Hat)
.where("user_id = ?")
# Q 1564 : # @user.wearable_hats
Query(Hat)
.where("user_id = ?")
# Q 1565 : # @message.short_id
Query(Message)
.select('short_id')
# Q 1566 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1567 : # message.recipient
Query(User)
.where("id = ?")
# Q 1568 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1569 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1570 : # message.recipient
Query(User)
.where("id = ?")
# Q 1571 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1572 : # message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 1573 : # message.recipient
Query(User)
.where("id = ?")
# Q 1574 : # self.link
Query(Hat)
.select('link')
# Q 1575 : # self.link
Query(Hat)
.select('link')
# Q 1576 : # Story.arel_table
Query(Story)

# Q 1577 : # Story.arel_table
Query(Story)

# Q 1578 : # Story.arel_table
Query(Story)

# Q 1579 : # @hat_request.approve_by_user!(@user)
Query(HatRequest)

# Q 1580 : # @hat_request.approve_by_user!
Query(HatRequest)

# Q 1581 : # @hat_request.approve_by_user!
Query(HatRequest)

# Q 1582 : # @user.authenticate(params[:user][:password].to_s)
Query(User)

# Q 1583 : # @user.authenticate
Query(User)

# Q 1584 : # @user.authenticate
Query(User)

# Q 1585 : # user.is_active?
Query(User)

# Q 1586 : # user.is_active?
Query(User)

# Q 1587 : # user.is_active?
Query(User)

# Q 1588 : # user.is_active?
Query(User)

# Q 1589 : # Tag.all_with_filtered_counts_for(@user).map
Query(Tag)

# Q 1590 : # Tag.all_with_filtered_counts_for
Query(Tag)

# Q 1591 : # story.merged_stories.each
Query(Story)
.where("story_id = ?")
# Q 1592 : # story.merged_stories
Query(Story)
.where("story_id = ?")
# Q 1593 : # @story.is_gone?
Query(Story)

# Q 1594 : # @story.is_undeletable_by_user?(@user)
Query(Story)

# Q 1595 : # @story.is_undeletable_by_user?
Query(Story)

# Q 1596 : # @story.is_gone?
Query(Story)

# Q 1597 : # @story.is_undeletable_by_user?
Query(Story)

# Q 1598 : # self.author
Query(User)
.where("id = ?")
# Q 1599 : # self.author
Query(User)
.where("id = ?")
# Q 1600 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1601 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1602 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1603 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1604 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1605 : # self.find_or_create_key_for_update(key, 0)
Query(Keystore)

# Q 1606 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1607 : # self.find_or_create_key_for_update
Query(Keystore)

# Q 1608 : # @invitation.destroy
Query(Invitation)

# Q 1609 : # @invitation.destroy
Query(Invitation)

# Q 1610 : # comment.valid?
Query(Comment)

# Q 1611 : # comment.save
Query(Comment)

# Q 1612 : # comment.valid?
Query(Comment)

# Q 1613 : # comment.save
Query(Comment)

# Q 1614 : # Story.where(:short_id => m[1]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 1615 : # Story.where(:short_id => m[1]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 1616 : # Story.where(:short_id => m[1])
Query(Story)
.where("short_id = ?")
# Q 1617 : # Story.where(:short_id => m[1]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 1618 : # Story.make!(:title => "flim flam", :url => "http://example.com/")
Query(Story)

# Q 1619 : # Story.make!
Query(Story)

# Q 1620 : # Story.make!(:title => "flim flam", :url => "http://example.com/")
Query(Story)

# Q 1621 : # Story.make!(:title => "flim flam", :url => "http://example.com/")
Query(Story)

# Q 1622 : # Story.make!
Query(Story)

# Q 1623 : # message.created_at
Query(Message)
.select('created_at')
# Q 1624 : # self.comment.to_s.strip.match(/\A(t)his([\.!])?$\z/i)
Query(Comment)
.select('comment')
# Q 1625 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1626 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1627 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1628 : # self.comment
Query(Comment)
.select('comment')
# Q 1629 : # self.comment.to_s.strip.match(/\A(t)his([\.!])?$\z/i)
Query(Comment)
.select('comment')
# Q 1630 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1631 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1632 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1633 : # self.comment
Query(Comment)
.select('comment')
# Q 1634 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1635 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1636 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1637 : # self.comment
Query(Comment)
.select('comment')
# Q 1638 : # self.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1639 : # self.author
Query(User)
.where("id = ?")
# Q 1640 : # self.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 1641 : # self.author
Query(User)
.where("id = ?")
# Q 1642 : # @user.can_submit_stories?
Query(User)

# Q 1643 : # @user.can_submit_stories?
Query(User)

# Q 1644 : # user.password_digest.to_s.match(/^\$2a\$#{
# BCrypt::Engine::DEFAULT_COST}\$/)
Query(User)
.select('password_digest')
# Q 1645 : # user.password_digest.to_s.match
Query(User)
.select('password_digest')
# Q 1646 : # user.password_digest.to_s
Query(User)
.select('password_digest')
# Q 1647 : # user.password_digest
Query(User)
.select('password_digest')
# Q 1648 : # user.password_digest.to_s.match
Query(User)
.select('password_digest')
# Q 1649 : # user.password_digest.to_s
Query(User)
.select('password_digest')
# Q 1650 : # user.password_digest
Query(User)
.select('password_digest')
# Q 1651 : # Story.count
Query(Story)

# Q 1652 : # Story.count
Query(Story)

# Q 1653 : # Story.count
Query(Story)

# Q 1654 : # Story.count
Query(Story)

# Q 1655 : # message.subject
Query(Message)
.select('subject')
# Q 1656 : # message.short_id
Query(Message)
.select('short_id')
# Q 1657 : # message.subject
Query(Message)
.select('subject')
# Q 1658 : # message.short_id
Query(Message)
.select('short_id')
# Q 1659 : # message.short_id
Query(Message)
.select('short_id')
# Q 1660 : # message.subject
Query(Message)
.select('subject')
# Q 1661 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1662 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1663 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1664 : # self.hat
Query(Hat)
.select('hat')
# Q 1665 : # self.hat
Query(Hat)
.select('hat')
# Q 1666 : # Message.new(message_params)
Query(Message)

# Q 1667 : # Message.new(message_params)
Query(Message)

# Q 1668 : # Message.new
Query(Message)

# Q 1669 : # Message.new
Query(Message)

# Q 1670 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1671 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1672 : # @user.hats
Query(Hat)
.where("user_id = ?")
# Q 1673 : # user.save
Query(User)

# Q 1674 : # user.save
Query(User)

# Q 1675 : # @user.id
Query(User)

# Q 1676 : # @user.id
Query(User)

# Q 1677 : # @user.id
Query(User)

# Q 1678 : # @user.has_2fa?
Query(User)

# Q 1679 : # @user.has_2fa?
Query(User)

# Q 1680 : # User.make!(:created_at => Time.now)
Query(User)

# Q 1681 : # User.make!
Query(User)

# Q 1682 : # User.make!(:created_at => Time.now)
Query(User)

# Q 1683 : # User.make!
Query(User)

# Q 1684 : # User.make!(:created_at => Time.now)
Query(User)

# Q 1685 : # User.make!
Query(User)

# Q 1686 : # User.make!
Query(User)

# Q 1687 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1688 : # Story.make!
Query(Story)

# Q 1689 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1690 : # Story.make!
Query(Story)

# Q 1691 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1692 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1693 : # Story.make!
Query(Story)

# Q 1694 : # Story.make!(:title => "flim flam 2", :url => "http://example.com/")
Query(Story)

# Q 1695 : # Story.make!
Query(Story)

# Q 1696 : # comment.hat_id
Query(Comment)
.select('hat_id')
# Q 1697 : # comment.hat_id
Query(Comment)
.select('hat_id')
# Q 1698 : # comment.hat_id
Query(Comment)
.select('hat_id')
# Q 1699 : # self.comment.to_s.strip.match(/\Atl;?dr.?$\z/i)
Query(Comment)
.select('comment')
# Q 1700 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1701 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1702 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1703 : # self.comment
Query(Comment)
.select('comment')
# Q 1704 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1705 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1706 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1707 : # self.comment
Query(Comment)
.select('comment')
# Q 1708 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1709 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1710 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 1711 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1712 : # @user.disable_2fa!
Query(User)

# Q 1713 : # @user.disable_2fa!
Query(User)

# Q 1714 : # User.exists?(:username => user[1..-1])
Query(User)
.return_limit('1')
# Q 1715 : # User.exists?
Query(User)
.return_limit('1')
# Q 1716 : # User.exists?
Query(User)
.return_limit('1')
# Q 1717 : # User.make!(:created_at => Time.now - 8.days)
Query(User)

# Q 1718 : # User.make!
Query(User)

# Q 1719 : # User.make!(:created_at => Time.now - 8.days)
Query(User)

# Q 1720 : # User.make!
Query(User)

# Q 1721 : # User.make!(:created_at => Time.now - 8.days)
Query(User)

# Q 1722 : # User.make!
Query(User)

# Q 1723 : # User.make!
Query(User)

# Q 1724 : # Story.make!
Query(Story)

# Q 1725 : # s = Story.make!
Query(Story)

# Q 1726 : # s = Story.make!
Query(Story)

# Q 1727 : # Story.make!
Query(Story)

# Q 1728 : # self.where(:user_id => user_id, :comment_id => nil, :story_id => story_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
.where("story_id = ?")
# Q 1729 : # self.where(:user_id => user_id, :comment_id => nil, :story_id => story_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
.where("story_id = ?")
# Q 1730 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1731 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1732 : # user.is_new?
Query(User)

# Q 1733 : # user.is_new?
Query(User)

# Q 1734 : # user.is_new?
Query(User)

# Q 1735 : # user.is_new?
Query(User)

# Q 1736 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1737 : # Comment.make!
Query(Comment)

# Q 1738 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1739 : # Comment.make!
Query(Comment)

# Q 1740 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 1741 : # Comment.make!
Query(Comment)

# Q 1742 : # Comment.make!
Query(Comment)

# Q 1743 : # @user.show_avatars?
Query(User)

# Q 1744 : # comment.id
Query(Comment)

# Q 1745 : # @story.is_gone?
Query(Story)

# Q 1746 : # @story.is_gone?
Query(Story)

# Q 1747 : # self.value_for(key)
Query(Keystore)

# Q 1748 : # self.value_for
Query(Keystore)

# Q 1749 : # self.value_for(key)
Query(Keystore)

# Q 1750 : # self.value_for
Query(Keystore)

# Q 1751 : # user.has_2fa?
Query(User)

# Q 1752 : # user.has_2fa?
Query(User)

# Q 1753 : # @story.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 1754 : # @story.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 1755 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1756 : # @story.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 1757 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 1758 : # @user.undeleted_received_messages
Query(User)

# Q 1759 : # @user.undeleted_received_messages
Query(User)

# Q 1760 : # @user.undeleted_received_messages
Query(User)

# Q 1761 : # stories.hidden
Query(Story)

# Q 1762 : # stories.hidden
Query(Story)

# Q 1763 : # Story.count
Query(Story)

# Q 1764 : # Story.count
Query(Story)

# Q 1765 : # Story.count
Query(Story)

# Q 1766 : # Story.count
Query(Story)

# Q 1767 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1768 : # comment.user
Query(User)
.where("id = ?")
# Q 1769 : # self.comment.to_s.strip.match(/\Ame too.?\z/i)
Query(Comment)
.select('comment')
# Q 1770 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1771 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1772 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1773 : # self.comment
Query(Comment)
.select('comment')
# Q 1774 : # self.comment.to_s.strip.match
Query(Comment)
.select('comment')
# Q 1775 : # self.comment.to_s.strip
Query(Comment)
.select('comment')
# Q 1776 : # self.comment.to_s
Query(Comment)
.select('comment')
# Q 1777 : # self.comment
Query(Comment)
.select('comment')
# Q 1778 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1779 : # HatRequest.find(params[:id])
Query(HatRequest)
.where("id = ?")
# Q 1780 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1781 : # HatRequest.find
Query(HatRequest)
.where("id = ?")
# Q 1782 : # user.session_token
Query(User)
.select('session_token')
# Q 1783 : # user.session_token
Query(User)
.select('session_token')
# Q 1784 : # user.session_token
Query(User)
.select('session_token')
# Q 1785 : # comment.user
Query(User)
.where("id = ?")
# Q 1786 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 1787 : # @story.id
Query(Story)

# Q 1788 : # @story.user_id
Query(Story)
.select('user_id')
# Q 1789 : # @user.id
Query(User)

# Q 1790 : # @user.is_moderator?
Query(User)

# Q 1791 : # @story.user_id
Query(Story)
.select('user_id')
# Q 1792 : # @user.id
Query(User)

# Q 1793 : # @user.is_moderator?
Query(User)

# Q 1794 : # @story.user_id
Query(Story)
.select('user_id')
# Q 1795 : # @user.id
Query(User)

# Q 1796 : # @user.is_moderator?
Query(User)

# Q 1797 : # self.deleted_by_author?
Query(Message)

# Q 1798 : # self.deleted_by_recipient?
Query(Message)

# Q 1799 : # self.deleted_by_author?
Query(Message)

# Q 1800 : # self.deleted_by_recipient?
Query(Message)

# Q 1801 : # @hat_request.reject_by_user_for_reason!(@user, params[:hat_request][:rejection_comment])
Query(HatRequest)

# Q 1802 : # @hat_request.reject_by_user_for_reason!
Query(HatRequest)

# Q 1803 : # @hat_request.reject_by_user_for_reason!
Query(HatRequest)

# Q 1804 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1805 : # Story.make!
Query(Story)

# Q 1806 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1807 : # Story.make!
Query(Story)

# Q 1808 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1809 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1810 : # Story.make!
Query(Story)

# Q 1811 : # Story.make!(:title => "flim flam 2", :url => "http://www.example.com/")
Query(Story)

# Q 1812 : # Story.make!
Query(Story)

# Q 1813 : # User.make!
Query(User)

# Q 1814 : # u = User.make!
Query(User)

# Q 1815 : # u = User.make!
Query(User)

# Q 1816 : # User.make!
Query(User)

# Q 1817 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1818 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1819 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1820 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1821 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1822 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1823 : # self.destroy
Query(Message)

# Q 1824 : # self.destroy
Query(Message)

# Q 1825 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 1826 : # @story.id
Query(Story)

# Q 1827 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1828 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1829 : # tagging.tag.css_class
Query(Tag)
.where("id = ?")
# Q 1830 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1831 : # votes.inject({ })
Query(Vote)

# Q 1832 : # votes.inject
Query(Vote)

# Q 1833 : # votes.inject
Query(Vote)

# Q 1834 : # User.make!(:banned)
Query(User)

# Q 1835 : # User.make!
Query(User)

# Q 1836 : # User.make!(:banned)
Query(User)

# Q 1837 : # User.make!
Query(User)

# Q 1838 : # User.make!(:banned)
Query(User)

# Q 1839 : # User.make!
Query(User)

# Q 1840 : # User.make!
Query(User)

# Q 1841 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 1842 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1843 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 1844 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 1845 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1846 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1847 : # comment.user
Query(User)
.where("id = ?")
# Q 1848 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1849 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1850 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1851 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1852 : # tagging.tag.description
Query(Tag)
.where("id = ?")
.select('description')
# Q 1853 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1854 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 1855 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 1856 : # user.session_token
Query(User)
.select('session_token')
# Q 1857 : # user.session_token
Query(User)
.select('session_token')
# Q 1858 : # user.session_token
Query(User)
.select('session_token')
# Q 1859 : # Story.new
Query(Story)

# Q 1860 : # Story.new
Query(Story)

# Q 1861 : # Story.new
Query(Story)

# Q 1862 : # User.first
Query(User)
.return_limit('1')
# Q 1863 : # User.first
Query(User)
.return_limit('1')
# Q 1864 : # User.first
Query(User)
.return_limit('1')
# Q 1865 : # User.first
Query(User)
.return_limit('1')
# Q 1866 : # Story.count
Query(Story)

# Q 1867 : # Story.count
Query(Story)

# Q 1868 : # Story.count
Query(Story)

# Q 1869 : # Story.count
Query(Story)

# Q 1870 : # comment.html_class_for_user
Query(Comment)

# Q 1871 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1872 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1873 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1874 : # @story.short_id
Query(Story)
.select('short_id')
# Q 1875 : # self.order("(upvotes - downvotes) < 0 ASC, confidence DESC").group_by(&:parent_comment_id)
Query(Comment)
.order('id')
.order('confidence')
.order('upvotes')
.order('downvotes')
# Q 1876 : # self.order("(upvotes - downvotes) < 0 ASC, confidence DESC").group_by(&:parent_comment_id)
Query(Comment)
.order('id')
.order('confidence')
.order('upvotes')
.order('downvotes')
# Q 1877 : # self.order("(upvotes - downvotes) < 0 ASC, confidence DESC").group_by
Query(Comment)
.order('id')
.order('confidence')
.order('upvotes')
.order('downvotes')
# Q 1878 : # self.order("(upvotes - downvotes) < 0 ASC, confidence DESC")
Query(Comment)
.order('id')
.order('confidence')
.order('upvotes')
.order('downvotes')
# Q 1879 : # self.order
Query(Comment)

# Q 1880 : # self.order("(upvotes - downvotes) < 0 ASC, confidence DESC").group_by
Query(Comment)
.order('id')
.order('confidence')
.order('upvotes')
.order('downvotes')
# Q 1881 : # self.order
Query(Comment)

# Q 1882 : # self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1883 : # self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1884 : # self.lock(true).where(:key => key)
Query(Keystore)
.where("key = ?")
# Q 1885 : # self.lock(true)
Query(Keystore)

# Q 1886 : # self.lock
Query(Keystore)

# Q 1887 : # kv = self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1888 : # self.lock(true).where(:key => key).first
Query(Keystore)
.where("key = ?")
.return_limit('1')
# Q 1889 : # self.lock
Query(Keystore)

# Q 1890 : # self.q.to_s.split(" ").reject { |w|
#   
#   if (
#   m = w.match(/^domain:(.+)$/))
#     
#     domain = m[1]
#   end
# }.join(" ")
Query(Search)

# Q 1891 : # self.q.to_s.split(" ").reject { |w|
#   
#   if (
#   m = w.match(/^domain:(.+)$/))
#     
#     domain = m[1]
#   end
# }.join(" ")
Query(Search)

# Q 1892 : # self.q.to_s.split(" ").reject { |w|
#   
#   if (
#   m = w.match(/^domain:(.+)$/))
#     
#     domain = m[1]
#   end
# }.join
Query(Search)

# Q 1893 : # self.q.to_s.split(" ").reject
Query(Search)

# Q 1894 : # self.q.to_s.split(" ")
Query(Search)

# Q 1895 : # self.q.to_s.split
Query(Search)

# Q 1896 : # self.q.to_s
Query(Search)

# Q 1897 : # self.q
Query(Search)

# Q 1898 : # self.q.to_s.split(" ").reject { |w|
#   
#   if (
#   m = w.match(/^domain:(.+)$/))
#     
#     domain = m[1]
#   end
# }.join
Query(Search)

# Q 1899 : # self.q.to_s.split(" ").reject
Query(Search)

# Q 1900 : # self.q.to_s.split
Query(Search)

# Q 1901 : # self.q.to_s
Query(Search)

# Q 1902 : # self.q
Query(Search)

# Q 1903 : # comment.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 1904 : # comment.user
Query(User)
.where("id = ?")
# Q 1905 : # self.recipient.update_unread_message_count!
Query(User)
.where("id = ?")
# Q 1906 : # self.recipient
Query(User)
.where("id = ?")
# Q 1907 : # self.recipient.update_unread_message_count!
Query(User)
.where("id = ?")
# Q 1908 : # self.recipient
Query(User)
.where("id = ?")
# Q 1909 : # Moderation.new
Query(Moderation)

# Q 1910 : # Moderation.new
Query(Moderation)

# Q 1911 : # Moderation.new
Query(Moderation)

# Q 1912 : # comment.is_editable_by_user?(@user)
Query(Comment)

# Q 1913 : # comment.is_editable_by_user?
Query(Comment)

# Q 1914 : # comment.is_editable_by_user?
Query(Comment)

# Q 1915 : # comment.hat
Query(Hat)
.where("id = ?")
# Q 1916 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1917 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1918 : # self.created_at
Query(Hat)
.select('created_at')
# Q 1919 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1920 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1921 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1922 : # Story.where(:id => keep_ids)
Query(Story)
.where("id = ?")
# Q 1923 : # User.make!
Query(User)

# Q 1924 : # u = User.make!
Query(User)

# Q 1925 : # u = User.make!
Query(User)

# Q 1926 : # User.make!
Query(User)

# Q 1927 : # Story.make!(:url => "http://example.com")
Query(Story)

# Q 1928 : # Story.make!
Query(Story)

# Q 1929 : # Story.make!(:url => "http://example.com")
Query(Story)

# Q 1930 : # Story.make!
Query(Story)

# Q 1931 : # Story.make!(:url => "http://example.com")
Query(Story)

# Q 1932 : # Story.make!
Query(Story)

# Q 1933 : # Story.make!
Query(Story)

# Q 1934 : # comment.hat.to_html_label
Query(Hat)
.where("id = ?")
# Q 1935 : # comment.hat
Query(Hat)
.where("id = ?")
# Q 1936 : # self.user_id
Query(Hat)
.select('user_id')
# Q 1937 : # self.user_id
Query(Hat)
.select('user_id')
# Q 1938 : # self.user_id
Query(Hat)
.select('user_id')
# Q 1939 : # self.create!
Query(Keystore)

# Q 1940 : # self.create!
Query(Keystore)

# Q 1941 : # self.create! do |kv|
#   
#   kv.key = key
#   kv.value = init
#   kv.save!
# end
Query(Keystore)

# Q 1942 : # self.create!
Query(Keystore)

# Q 1943 : # self.granted_by_user_id
Query(Hat)
.select('granted_by_user_id')
# Q 1944 : # self.granted_by_user_id
Query(Hat)
.select('granted_by_user_id')
# Q 1945 : # self.granted_by_user_id
Query(Hat)
.select('granted_by_user_id')
# Q 1946 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1947 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1948 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 1949 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 1950 : # stories.hottest
Query(Story)

# Q 1951 : # stories.hottest
Query(Story)

# Q 1952 : # self.hat
Query(Hat)
.select('hat')
# Q 1953 : # self.link.present?
Query(Hat)
.select('link')
# Q 1954 : # self.link
Query(Hat)
.select('link')
# Q 1955 : # self.hat
Query(Hat)
.select('hat')
# Q 1956 : # self.link.present?
Query(Hat)
.select('link')
# Q 1957 : # self.link
Query(Hat)
.select('link')
# Q 1958 : # Story.make!(:url => "http://www3.example.com/goose")
Query(Story)

# Q 1959 : # Story.make!
Query(Story)

# Q 1960 : # Story.make!(:url => "http://www3.example.com/goose")
Query(Story)

# Q 1961 : # Story.make!
Query(Story)

# Q 1962 : # Story.make!(:url => "http://www3.example.com/goose")
Query(Story)

# Q 1963 : # Story.make!
Query(Story)

# Q 1964 : # Story.make!
Query(Story)

# Q 1965 : # comment.previewing
Query(Comment)

# Q 1966 : # @user.show_avatars?
Query(User)

# Q 1967 : # @user && @user.show_avatars?
Query(User)

# Q 1968 : # @user.show_avatars?
Query(User)

# Q 1969 : # self.link
Query(Hat)
.select('link')
# Q 1970 : # self.link
Query(Hat)
.select('link')
# Q 1971 : # InvitationRequest.new(params.require(:invitation_request).permit(:name, :email, :memo))
Query(InvitationRequest)

# Q 1972 : # InvitationRequest.new(params.require(:invitation_request).permit(:name, :email, :memo))
Query(InvitationRequest)

# Q 1973 : # InvitationRequest.new
Query(InvitationRequest)

# Q 1974 : # InvitationRequest.new
Query(InvitationRequest)

# Q 1975 : # @message.subject
Query(Message)
.select('subject')
# Q 1976 : # @message.subject
Query(Message)
.select('subject')
# Q 1977 : # @message.subject
Query(Message)
.select('subject')
# Q 1978 : # Story.make!(:title => "ti1", :url => "https://a.com/1", :user_id => u.id, :user_is_author => true)
Query(Story)

# Q 1979 : # Story.make!
Query(Story)

# Q 1980 : # Story.make!(:title => "ti1", :url => "https://a.com/1", :user_id => u.id, :user_is_author => true)
Query(Story)

# Q 1981 : # Story.make!(:title => "ti1", :url => "https://a.com/1", :user_id => u.id, :user_is_author => true)
Query(Story)

# Q 1982 : # Story.make!
Query(Story)

# Q 1983 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, s.id, c.id, u.id, Vote::COMMENT_REASONS.keys.first)
Query(Vote)

# Q 1984 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1985 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, s.id, c.id, u.id, Vote::COMMENT_REASONS.keys.first)
Query(Vote)

# Q 1986 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, s.id, c.id, u.id, Vote::COMMENT_REASONS.keys.first)
Query(Vote)

# Q 1987 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 1988 : # self.recipient.email_messages?
Query(User)
.where("id = ?")
# Q 1989 : # self.recipient
Query(User)
.where("id = ?")
# Q 1990 : # self.recipient.email_messages?
Query(User)
.where("id = ?")
# Q 1991 : # self.recipient
Query(User)
.where("id = ?")
# Q 1992 : # stories.order("stories.created_at DESC")
Query(Story)
.order('id')
.order('created_at')
# Q 1993 : # stories.order
Query(Story)

# Q 1994 : # stories.order
Query(Story)

# Q 1995 : # ReadRibbon.where(user_id: @user.id, story_id: story_ids).update_all(updated_at: Time.now)
Query(ReadRibbon)
.where("user_id = ?")
.where("story_id = ?")
# Q 1996 : # ReadRibbon.where(user_id: @user.id, story_id: story_ids).update_all
Query(ReadRibbon)
.where("user_id = ?")
.where("story_id = ?")
# Q 1997 : # ReadRibbon.where(user_id: @user.id, story_id: story_ids)
Query(ReadRibbon)
.where("user_id = ?")
.where("story_id = ?")
# Q 1998 : # ReadRibbon.where(user_id: @user.id, story_id: story_ids).update_all
Query(ReadRibbon)
.where("user_id = ?")
.where("story_id = ?")
# Q 1999 : # self.where(:user_id => user_id, :comment_id => comment_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
# Q 2000 : # self.where(:user_id => user_id, :comment_id => comment_ids)
Query(Vote)
.where("user_id = ?")
.where("comment_id = ?")
# Q 2001 : # @message.author
Query(User)
.where("id = ?")
# Q 2002 : # @message.author
Query(User)
.where("id = ?")
# Q 2003 : # @user.id
Query(User)

# Q 2004 : # @user.id
Query(User)

# Q 2005 : # Story.make!(:url => "http://flub.example.com")
Query(Story)

# Q 2006 : # Story.make!
Query(Story)

# Q 2007 : # Story.make!(:url => "http://flub.example.com")
Query(Story)

# Q 2008 : # Story.make!
Query(Story)

# Q 2009 : # Story.make!(:url => "http://flub.example.com")
Query(Story)

# Q 2010 : # Story.make!
Query(Story)

# Q 2011 : # Story.make!
Query(Story)

# Q 2012 : # self.recipient
Query(User)
.where("id = ?")
# Q 2013 : # self.recipient
Query(User)
.where("id = ?")
# Q 2014 : # self.what
Query(Search)

# Q 2015 : # self.what
Query(Search)

# Q 2016 : # Story.new
Query(Story)

# Q 2017 : # Story.new
Query(Story)

# Q 2018 : # Story.new
Query(Story)

# Q 2019 : # Message.new
Query(Message)

# Q 2020 : # Message.new
Query(Message)

# Q 2021 : # Message.new
Query(Message)

# Q 2022 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2023 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2024 : # comment.has_been_edited?
Query(Comment)

# Q 2025 : # if story.user_is_author?
#   
#   
# else
#   
#   
# end
Query(Story)

# Q 2026 : # story.user_is_author?
Query(Story)

# Q 2027 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2028 : # @user.id
Query(User)

# Q 2029 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2030 : # @user.id
Query(User)

# Q 2031 : # self.recipient.email
Query(User)
.where("id = ?")
.select('email')
# Q 2032 : # self.recipient
Query(User)
.where("id = ?")
# Q 2033 : # self.recipient.email
Query(User)
.where("id = ?")
.select('email')
# Q 2034 : # self.recipient
Query(User)
.where("id = ?")
# Q 2035 : # where(:banned_at => nil, :deleted_at => nil)
Query(User)
.where("banned_at = ?")
.where("deleted_at = ?")
# Q 2036 : # Story.unmerged.where(:is_expired => false).includes({ :taggings => :tag }, :user)
Query(Story)
.where("is_expired = ?")
.includes('user')
# Q 2037 : # Story.unmerged.where(:is_expired => false).includes({ :taggings => :tag }, :user)
Query(Story)
.where("is_expired = ?")
.includes('user')
# Q 2038 : # Story.unmerged.where(:is_expired => false).includes
Query(Story)
.where("is_expired = ?")
# Q 2039 : # Story.unmerged.where(:is_expired => false)
Query(Story)
.where("is_expired = ?")
# Q 2040 : # Story.unmerged.where
Query(Story)

# Q 2041 : # Story.unmerged
Query(Story)

# Q 2042 : # Story.unmerged.where(:is_expired => false).includes
Query(Story)
.where("is_expired = ?")
# Q 2043 : # Story.unmerged.where
Query(Story)

# Q 2044 : # Story.unmerged
Query(Story)

# Q 2045 : # @invitation_request.save
Query(InvitationRequest)

# Q 2046 : # @invitation_request.save
Query(InvitationRequest)

# Q 2047 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 2048 : # @message.recipient
Query(User)
.where("id = ?")
# Q 2049 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 2050 : # @message.author
Query(User)
.where("id = ?")
# Q 2051 : # @message.recipient.username
Query(User)
.where("id = ?")
.select('username')
# Q 2052 : # @message.recipient
Query(User)
.where("id = ?")
# Q 2053 : # @message.author.username
Query(User)
.where("id = ?")
.select('username')
# Q 2054 : # @message.author
Query(User)
.where("id = ?")
# Q 2055 : # Story.make!(:title => "ti2", :url => "https://a.com/2", :user_id => u.id, :user_is_author => true)
Query(Story)

# Q 2056 : # Story.make!
Query(Story)

# Q 2057 : # Story.make!(:title => "ti2", :url => "https://a.com/2", :user_id => u.id, :user_is_author => true)
Query(Story)

# Q 2058 : # Story.make!(:title => "ti2", :url => "https://a.com/2", :user_id => u.id, :user_is_author => true)
Query(Story)

# Q 2059 : # Story.make!
Query(Story)

# Q 2060 : # comment.is_from_email?
Query(Comment)

# Q 2061 : # where("
#       is_moderator = True OR
#       users.id IN (select distinct moderator_user_id from moderations)
#   ")
Query(User)
.where(" = ?")
# Q 2062 : # votes.inject({ })
Query(Vote)

# Q 2063 : # votes.inject
Query(Vote)

# Q 2064 : # votes.inject
Query(Vote)

# Q 2065 : # Story.arel_table
Query(Story)

# Q 2066 : # Story.arel_table
Query(Story)

# Q 2067 : # @message.subject.match(/^re:/i)
Query(Message)
.select('subject')
# Q 2068 : # @message.subject.match
Query(Message)
.select('subject')
# Q 2069 : # @message.subject
Query(Message)
.select('subject')
# Q 2070 : # @message.subject.match
Query(Message)
.select('subject')
# Q 2071 : # @message.subject
Query(Message)
.select('subject')
# Q 2072 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2073 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2074 : # Story.make!(:title => "Hello there, this is a title")
Query(Story)

# Q 2075 : # Story.make!
Query(Story)

# Q 2076 : # Story.make!(:title => "Hello there, this is a title")
Query(Story)

# Q 2077 : # Story.make!
Query(Story)

# Q 2078 : # Story.make!(:title => "Hello there, this is a title")
Query(Story)

# Q 2079 : # Story.make!
Query(Story)

# Q 2080 : # Story.make!
Query(Story)

# Q 2081 : # @message.subject
Query(Message)
.select('subject')
# Q 2082 : # @message.subject
Query(Message)
.select('subject')
# Q 2083 : # @message.subject
Query(Message)
.select('subject')
# Q 2084 : # comment.as_json
Query(Comment)

# Q 2085 : # comment.as_json
Query(Comment)

# Q 2086 : # self.recipient.pushover_messages?
Query(User)
.where("id = ?")
# Q 2087 : # self.recipient
Query(User)
.where("id = ?")
# Q 2088 : # self.recipient.pushover_messages?
Query(User)
.where("id = ?")
# Q 2089 : # self.recipient
Query(User)
.where("id = ?")
# Q 2090 : # self.increment_value_for(key, amount)
Query(Keystore)

# Q 2091 : # self.increment_value_for
Query(Keystore)

# Q 2092 : # self.increment_value_for
Query(Keystore)

# Q 2093 : # @user.unread_replies_count
Query(User)

# Q 2094 : # @user.unread_replies_count
Query(User)

# Q 2095 : # @user.unread_replies_count
Query(User)

# Q 2096 : # @story.fetched_attributes
Query(Story)

# Q 2097 : # @story.fetched_attributes
Query(Story)

# Q 2098 : # @story.fetched_attributes
Query(Story)

# Q 2099 : # self.recipient.pushover!({ :title => "#{
# Rails.application.name} message from " << "#{
# self.author_username}: #{
# self.subject}", :message => self.plaintext_body, :url => self.url, :url_title => (
# self.author ? "Reply to #{
# self.author_username}" : "View message") })
Query(User)
.where("id = ?")
# Q 2100 : # self.recipient.pushover!
Query(User)
.where("id = ?")
# Q 2101 : # self.recipient
Query(User)
.where("id = ?")
# Q 2102 : # self.recipient.pushover!
Query(User)
.where("id = ?")
# Q 2103 : # self.recipient
Query(User)
.where("id = ?")
# Q 2104 : # if self.url.present?
#   
#   check_already_posted
#   check_not_tracking_domain
#   unless self.url.match(/\Ahttps?:\/\/([^\.]+\.)+[a-z]+(\/|\z)/i)
#     
#     errors.add(:url, "is not valid")
#   end
# elsif self.description.to_s.strip == ""
#   
#   errors.add(:description, "must contain text if no URL posted")
# end
Query(Story)

# Q 2105 : # self.url.present?
Query(Story)
.select('url')
# Q 2106 : # self.url
Query(Story)
.select('url')
# Q 2107 : # @message.subject
Query(Message)
.select('subject')
# Q 2108 : # @message.subject
Query(Message)
.select('subject')
# Q 2109 : # Story.make!(:title => "ti3", :url => "https://a.com/3", :user_id => u.id, :user_is_author => false)
Query(Story)

# Q 2110 : # Story.make!
Query(Story)

# Q 2111 : # Story.make!(:title => "ti3", :url => "https://a.com/3", :user_id => u.id, :user_is_author => false)
Query(Story)

# Q 2112 : # Story.make!(:title => "ti3", :url => "https://a.com/3", :user_id => u.id, :user_is_author => false)
Query(Story)

# Q 2113 : # Story.make!
Query(Story)

# Q 2114 : # Story.make!(:title => "Hello _ underscore")
Query(Story)

# Q 2115 : # Story.make!
Query(Story)

# Q 2116 : # Story.make!(:title => "Hello _ underscore")
Query(Story)

# Q 2117 : # Story.make!
Query(Story)

# Q 2118 : # Story.make!(:title => "Hello _ underscore")
Query(Story)

# Q 2119 : # Story.make!
Query(Story)

# Q 2120 : # Story.make!
Query(Story)

# Q 2121 : # Story.make!
Query(Story)

# Q 2122 : # s = Story.make!
Query(Story)

# Q 2123 : # s = Story.make!
Query(Story)

# Q 2124 : # Story.make!
Query(Story)

# Q 2125 : # user.is_moderator?
Query(User)

# Q 2126 : # user.id
Query(User)

# Q 2127 : # user.is_moderator?
Query(User)

# Q 2128 : # user.id
Query(User)

# Q 2129 : # @story.url
Query(Story)
.select('url')
# Q 2130 : # @story.url
Query(Story)
.select('url')
# Q 2131 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2132 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2133 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 2134 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2135 : # @user.email
Query(User)
.select('email')
# Q 2136 : # @user.email
Query(User)
.select('email')
# Q 2137 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 2138 : # Comment.make!
Query(Comment)

# Q 2139 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 2140 : # Comment.make!
Query(Comment)

# Q 2141 : # Comment.make!(:story_id => s.id)
Query(Comment)

# Q 2142 : # Comment.make!
Query(Comment)

# Q 2143 : # Comment.make!
Query(Comment)

# Q 2144 : # comment.has_been_edited?
Query(Comment)

# Q 2145 : # self.author_username
Query(Message)

# Q 2146 : # self.subject
Query(Message)
.select('subject')
# Q 2147 : # self.author_username
Query(Message)

# Q 2148 : # self.subject
Query(Message)
.select('subject')
# Q 2149 : # comment.updated_at
Query(Comment)
.select('updated_at')
# Q 2150 : # comment.created_at
Query(Comment)
.select('created_at')
# Q 2151 : # self.plaintext_body
Query(Message)

# Q 2152 : # self.plaintext_body
Query(Message)

# Q 2153 : # self.create_rss_token
Query(User)

# Q 2154 : # self.create_rss_token
Query(User)

# Q 2155 : # self.incremented_value_for(key, amount)
Query(Keystore)

# Q 2156 : # self.incremented_value_for
Query(Keystore)

# Q 2157 : # self.incremented_value_for
Query(Keystore)

# Q 2158 : # comment.url
Query(Comment)

# Q 2159 : # comment.url
Query(Comment)

# Q 2160 : # Story.make!(:title => "Hello, underscore")
Query(Story)

# Q 2161 : # Story.make!
Query(Story)

# Q 2162 : # Story.make!(:title => "Hello, underscore")
Query(Story)

# Q 2163 : # Story.make!
Query(Story)

# Q 2164 : # Story.make!(:title => "Hello, underscore")
Query(Story)

# Q 2165 : # Story.make!
Query(Story)

# Q 2166 : # Story.make!
Query(Story)

# Q 2167 : # User.make!
Query(User)

# Q 2168 : # u = User.make!
Query(User)

# Q 2169 : # u = User.make!
Query(User)

# Q 2170 : # User.make!
Query(User)

# Q 2171 : # self.url
Query(Message)

# Q 2172 : # self.url
Query(Message)

# Q 2173 : # self.create_mailing_list_token
Query(User)

# Q 2174 : # self.create_mailing_list_token
Query(User)

# Q 2175 : # self.url.match(/\Ahttps?:\/\/([^\.]+\.)+[a-z]+(\/|\z)/i)
Query(Story)
.select('url')
# Q 2176 : # self.url.match
Query(Story)
.select('url')
# Q 2177 : # self.url
Query(Story)
.select('url')
# Q 2178 : # self.url.match
Query(Story)
.select('url')
# Q 2179 : # self.url
Query(Story)
.select('url')
# Q 2180 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2181 : # @user.id
Query(User)

# Q 2182 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2183 : # @user.id
Query(User)

# Q 2184 : # self.author
Query(User)
.where("id = ?")
# Q 2185 : # self.author_username
Query(Message)

# Q 2186 : # self.author
Query(User)
.where("id = ?")
# Q 2187 : # self.author_username
Query(Message)

# Q 2188 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id).first_or_initialize
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2189 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id).first_or_initialize
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2190 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2191 : # Vote.where(:user_id => user_id, :story_id => story_id, :comment_id => comment_id).first_or_initialize
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 2192 : # Story.make!(:title => "ti4", :url => "https://a.com/4", :user_id => u.id, :user_is_author => false)
Query(Story)

# Q 2193 : # Story.make!
Query(Story)

# Q 2194 : # Story.make!(:title => "ti4", :url => "https://a.com/4", :user_id => u.id, :user_is_author => false)
Query(Story)

# Q 2195 : # Story.make!(:title => "ti4", :url => "https://a.com/4", :user_id => u.id, :user_is_author => false)
Query(Story)

# Q 2196 : # Story.make!
Query(Story)

# Q 2197 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2198 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2199 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2200 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2201 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2202 : # comment.previewing
Query(Comment)

# Q 2203 : # @message.save
Query(Message)

# Q 2204 : # @message.save
Query(Message)

# Q 2205 : # Story.make(:title => "The One-second War (What Time Will You Die?) ")
Query(Story)

# Q 2206 : # Story.make
Query(Story)

# Q 2207 : # Story.make(:title => "The One-second War (What Time Will You Die?) ")
Query(Story)

# Q 2208 : # Story.make
Query(Story)

# Q 2209 : # Story.make(:title => "The One-second War (What Time Will You Die?) ")
Query(Story)

# Q 2210 : # Story.make
Query(Story)

# Q 2211 : # Story.make
Query(Story)

# Q 2212 : # self.description.to_s.strip
Query(Story)
.select('description')
# Q 2213 : # self.description.to_s
Query(Story)
.select('description')
# Q 2214 : # self.description
Query(Story)
.select('description')
# Q 2215 : # Story.arel_table
Query(Story)

# Q 2216 : # Story.arel_table
Query(Story)

# Q 2217 : # Story.find_similar_by_url(@story.url)
Query(Story)

# Q 2218 : # Story.find_similar_by_url(@story.url)
Query(Story)

# Q 2219 : # Story.find_similar_by_url
Query(Story)

# Q 2220 : # @story.url
Query(Story)
.select('url')
# Q 2221 : # Story.find_similar_by_url
Query(Story)

# Q 2222 : # @story.url
Query(Story)
.select('url')
# Q 2223 : # @user.username
Query(User)
.select('username')
# Q 2224 : # @user.username
Query(User)
.select('username')
# Q 2225 : # @user.username
Query(User)
.select('username')
# Q 2226 : # @user.username
Query(User)
.select('username')
# Q 2227 : # @user.username
Query(User)
.select('username')
# Q 2228 : # comment.url
Query(Comment)

# Q 2229 : # Tagging.arel_table
Query(Tagging)

# Q 2230 : # Tagging.arel_table
Query(Tagging)

# Q 2231 : # @user.unread_message_count
Query(User)

# Q 2232 : # @user.unread_message_count
Query(User)

# Q 2233 : # @user.unread_message_count
Query(User)

# Q 2234 : # @user.can_see_invitation_requests?
Query(User)

# Q 2235 : # @user.can_see_invitation_requests?
Query(User)

# Q 2236 : # Tagging.arel_table
Query(Tagging)

# Q 2237 : # tag.id
Query(Tag)

# Q 2238 : # Tagging.arel_table
Query(Tagging)

# Q 2239 : # tag.id
Query(Tag)

# Q 2240 : # comment.is_editable_by_user?
Query(Comment)

# Q 2241 : # comment.is_editable_by_user?(@user)
Query(Comment)

# Q 2242 : # comment.is_editable_by_user?
Query(Comment)

# Q 2243 : # comment.is_editable_by_user?
Query(Comment)

# Q 2244 : # self.url.blank?
Query(Story)
.select('url')
# Q 2245 : # self.url
Query(Story)
.select('url')
# Q 2246 : # self.url.blank?
Query(Story)
.select('url')
# Q 2247 : # self.url
Query(Story)
.select('url')
# Q 2248 : # Tagging.arel_table
Query(Tagging)

# Q 2249 : # Tagging.arel_table
Query(Tagging)

# Q 2250 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2251 : # @user.id
Query(User)

# Q 2252 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2253 : # @user.id
Query(User)

# Q 2254 : # User.make!
Query(User)

# Q 2255 : # u = User.make!
Query(User)

# Q 2256 : # u = User.make!
Query(User)

# Q 2257 : # User.make!
Query(User)

# Q 2258 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2259 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2260 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2261 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, s.id, c.id, u.id, nil)
Query(Vote)

# Q 2262 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2263 : # @user.show_story_previews?
Query(User)

# Q 2264 : # Story.make!(:user_id => u.id)
Query(Story)

# Q 2265 : # Story.make!
Query(Story)

# Q 2266 : # Story.make!(:user_id => u.id)
Query(Story)

# Q 2267 : # Story.make!
Query(Story)

# Q 2268 : # Story.make!(:user_id => u.id)
Query(Story)

# Q 2269 : # Story.make!
Query(Story)

# Q 2270 : # Story.make!
Query(Story)

# Q 2271 : # story.description_or_story_cache
Query(Story)

# Q 2272 : # User.where(:username => username).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2273 : # User.where(:username => username).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2274 : # User.where(:username => username)
Query(User)
.where("username = ?")
# Q 2275 : # User.where(:username => username).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2276 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2277 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2278 : # InvitationRequest.where(:code => params[:code].to_s)
Query(InvitationRequest)
.where("code = ?")
# Q 2279 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2280 : # comment.is_gone?
Query(Comment)

# Q 2281 : # comment.is_undeletable_by_user?
Query(Comment)

# Q 2282 : # @user.can_see_invitation_requests?
Query(User)

# Q 2283 : # Vote.transaction
Query(Vote)

# Q 2284 : # Vote.transaction
Query(Vote)

# Q 2285 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2286 : # @user.id
Query(User)

# Q 2287 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2288 : # @user.id
Query(User)

# Q 2289 : # InvitationRequest.verified_count
Query(InvitationRequest)

# Q 2290 : # User.make!
Query(User)

# Q 2291 : # u = User.make!
Query(User)

# Q 2292 : # u = User.make!
Query(User)

# Q 2293 : # User.make!
Query(User)

# Q 2294 : # tag.tag
Query(Tag)
.select('tag')
# Q 2295 : # @user.username
Query(User)
.select('username')
# Q 2296 : # @user.karma
Query(User)
.select('karma')
# Q 2297 : # @user.username
Query(User)
.select('username')
# Q 2298 : # @user.karma
Query(User)
.select('karma')
# Q 2299 : # comment.is_gone?
Query(Comment)

# Q 2300 : # comment.is_deletable_by_user?
Query(Comment)

# Q 2301 : # tag.css_class
Query(Tag)

# Q 2302 : # tag.description
Query(Tag)
.select('description')
# Q 2303 : # @user.is_moderator?
Query(User)

# Q 2304 : # tag.tag
Query(Tag)
.select('tag')
# Q 2305 : # self.url.present?
Query(Story)
.select('url')
# Q 2306 : # self.url
Query(Story)
.select('url')
# Q 2307 : # self.new_record?
Query(Story)

# Q 2308 : # self.url.present?
Query(Story)
.select('url')
# Q 2309 : # self.url
Query(Story)
.select('url')
# Q 2310 : # self.new_record?
Query(Story)

# Q 2311 : # Invitation.new
Query(Invitation)

# Q 2312 : # Invitation.new
Query(Invitation)

# Q 2313 : # Invitation.new
Query(Invitation)

# Q 2314 : # @message.save!
Query(Message)

# Q 2315 : # @message.save!
Query(Message)

# Q 2316 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2317 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2318 : # User.where(:username => params[:username])
Query(User)
.where("username = ?")
# Q 2319 : # User.where(:username => params[:username]).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2320 : # @user.is_moderator?
Query(User)

# Q 2321 : # @user.id
Query(User)

# Q 2322 : # comment.user_id
Query(Comment)
.select('user_id')
# Q 2323 : # HatRequest.count
Query(HatRequest)

# Q 2324 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 2325 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 2326 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s)
Query(User)
.where(" = ?")
# Q 2327 : # User.where("email = ? OR username = ?", params[:email].to_s, params[:email].to_s).first
Query(User)
.where(" = ?")
.return_limit('1')
# Q 2328 : # @user.id
Query(User)

# Q 2329 : # @user.id
Query(User)

# Q 2330 : # @user.id
Query(User)

# Q 2331 : # Story.find_similar_by_url(self.url)
Query(Story)

# Q 2332 : # Story.find_similar_by_url(self.url)
Query(Story)

# Q 2333 : # Story.find_similar_by_url
Query(Story)

# Q 2334 : # self.url
Query(Story)
.select('url')
# Q 2335 : # Story.find_similar_by_url
Query(Story)

# Q 2336 : # self.url
Query(Story)
.select('url')
# Q 2337 : # Story.score_sql
Query(Story)

# Q 2338 : # Story.score_sql
Query(Story)

# Q 2339 : # @story.title.present?
Query(Story)
.select('title')
# Q 2340 : # @story.title
Query(Story)
.select('title')
# Q 2341 : # @story.title.present?
Query(Story)
.select('title')
# Q 2342 : # @story.title
Query(Story)
.select('title')
# Q 2343 : # Story.make
Query(Story)

# Q 2344 : # s = Story.make
Query(Story)

# Q 2345 : # s = Story.make
Query(Story)

# Q 2346 : # Story.make
Query(Story)

# Q 2347 : # @user.show_avatars?
Query(User)

# Q 2348 : # stories.newest
Query(Story)

# Q 2349 : # stories.newest
Query(Story)

# Q 2350 : # @user.username
Query(User)
.select('username')
# Q 2351 : # @user.username
Query(User)
.select('username')
# Q 2352 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2353 : # story.user
Query(User)
.where("id = ?")
# Q 2354 : # self.body
Query(Message)
.select('body')
# Q 2355 : # self.body
Query(Message)
.select('body')
# Q 2356 : # self.already_posted_story&.is_recent?
Query(Story)

# Q 2357 : # self.already_posted_story
Query(Story)

# Q 2358 : # self.already_posted_story&.is_recent?
Query(Story)

# Q 2359 : # self.already_posted_story
Query(Story)

# Q 2360 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2361 : # @user.id
Query(User)

# Q 2362 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2363 : # @user.id
Query(User)

# Q 2364 : # Comment.new
Query(Comment)

# Q 2365 : # Comment.new
Query(Comment)

# Q 2366 : # Comment.new
Query(Comment)

# Q 2367 : # story.user
Query(User)
.where("id = ?")
# Q 2368 : # self.order
Query(Search)

# Q 2369 : # self.order
Query(Search)

# Q 2370 : # story.previewing
Query(Story)

# Q 2371 : # Story.make
Query(Story)

# Q 2372 : # s = Story.make
Query(Story)

# Q 2373 : # s = Story.make
Query(Story)

# Q 2374 : # Story.make
Query(Story)

# Q 2375 : # comment.story.is_gone?
Query(Story)
.where("id = ?")
# Q 2376 : # comment.story
Query(Story)
.where("id = ?")
# Q 2377 : # comment.is_gone?
Query(Comment)

# Q 2378 : # story.user_is_author?
Query(Story)

# Q 2379 : # Comment.all.each
Query(Comment)

# Q 2380 : # Comment.all
Query(Comment)

# Q 2381 : # Comment.all.each
Query(Comment)

# Q 2382 : # Comment.all
Query(Comment)

# Q 2383 : # Story.unmerged.where(is_expired: false)
Query(Story)
.where("is_expired = ?")
# Q 2384 : # Story.unmerged.where
Query(Story)

# Q 2385 : # Story.unmerged
Query(Story)

# Q 2386 : # Story.unmerged.where
Query(Story)

# Q 2387 : # Story.unmerged
Query(Story)

# Q 2388 : # self.body.to_s
Query(Message)
.select('body')
# Q 2389 : # self.body
Query(Message)
.select('body')
# Q 2390 : # self.body.to_s
Query(Message)
.select('body')
# Q 2391 : # self.body
Query(Message)
.select('body')
# Q 2392 : # self.results.order!
Query(Search)

# Q 2393 : # self.results
Query(Search)

# Q 2394 : # self.results.order!
Query(Search)

# Q 2395 : # self.results
Query(Search)

# Q 2396 : # Story.new(story_params)
Query(Story)

# Q 2397 : # Story.new(story_params)
Query(Story)

# Q 2398 : # Story.new
Query(Story)

# Q 2399 : # Story.new
Query(Story)

# Q 2400 : # @user.id
Query(User)

# Q 2401 : # @user.id
Query(User)

# Q 2402 : # @user.id
Query(User)

# Q 2403 : # @user.id
Query(User)

# Q 2404 : # @user.id
Query(User)

# Q 2405 : # self.url.present?
Query(Story)
.select('url')
# Q 2406 : # self.url
Query(Story)
.select('url')
# Q 2407 : # self.new_record?
Query(Story)

# Q 2408 : # self.url.present?
Query(Story)
.select('url')
# Q 2409 : # self.url
Query(Story)
.select('url')
# Q 2410 : # self.new_record?
Query(Story)

# Q 2411 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2412 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2413 : # @user.authenticate_totp(params[:totp_code])
Query(User)

# Q 2414 : # @user.authenticate_totp
Query(User)

# Q 2415 : # @user.authenticate_totp
Query(User)

# Q 2416 : # story.html_class_for_user
Query(Story)

# Q 2417 : # self.short_id
Query(Message)
.select('short_id')
# Q 2418 : # self.short_id
Query(Message)
.select('short_id')
# Q 2419 : # self.url.match(/\Ahttps?:\/\/([^\/]+)/i)
Query(Story)
.select('url')
# Q 2420 : # self.url.match(/\Ahttps?:\/\/([^\/]+)/i)
Query(Story)
.select('url')
# Q 2421 : # self.url.match
Query(Story)
.select('url')
# Q 2422 : # self.url
Query(Story)
.select('url')
# Q 2423 : # self.url.match
Query(Story)
.select('url')
# Q 2424 : # self.url
Query(Story)
.select('url')
# Q 2425 : # Vote.new(:vote => 1)
Query(Vote)

# Q 2426 : # Vote.new(:vote => 1)
Query(Vote)

# Q 2427 : # Vote.new
Query(Vote)

# Q 2428 : # Vote.new
Query(Vote)

# Q 2429 : # comment.is_deletable_by_user?(@user)
Query(Comment)

# Q 2430 : # comment.is_deletable_by_user?
Query(Comment)

# Q 2431 : # comment.is_deletable_by_user?
Query(Comment)

# Q 2432 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2433 : # story.user
Query(User)
.where("id = ?")
# Q 2434 : # Story.make(:title => "blah")
Query(Story)

# Q 2435 : # Story.make
Query(Story)

# Q 2436 : # Story.make(:title => "blah")
Query(Story)

# Q 2437 : # Story.make
Query(Story)

# Q 2438 : # Story.make(:title => "blah")
Query(Story)

# Q 2439 : # Story.make
Query(Story)

# Q 2440 : # Story.make
Query(Story)

# Q 2441 : # comment.story.comments_path
Query(Story)
.where("id = ?")
# Q 2442 : # comment.story
Query(Story)
.where("id = ?")
# Q 2443 : # comment.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 2444 : # comment.story
Query(Story)
.where("id = ?")
# Q 2445 : # User.all.each
Query(User)

# Q 2446 : # User.all
Query(User)

# Q 2447 : # User.all.each
Query(User)

# Q 2448 : # User.all
Query(User)

# Q 2449 : # self.results.order!
Query(Search)

# Q 2450 : # self.results
Query(Search)

# Q 2451 : # self.results.order!
Query(Search)

# Q 2452 : # self.results
Query(Search)

# Q 2453 : # @user.save!
Query(User)

# Q 2454 : # @user.save!
Query(User)

# Q 2455 : # hat.to_html_label
Query(Hat)

# Q 2456 : # hat.to_html_label
Query(Hat)

# Q 2457 : # @story.valid?
Query(Story)

# Q 2458 : # @story.valid?
Query(Story)

# Q 2459 : # @user.can_see_invitation_requests?
Query(User)

# Q 2460 : # @user.can_see_invitation_requests?
Query(User)

# Q 2461 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2462 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2463 : # Message.where(:short_id => m[1])
Query(Message)
.where("short_id = ?")
# Q 2464 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2465 : # Message.where(:short_id => m[1])
Query(Message)
.where("short_id = ?")
# Q 2466 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2467 : # Message.where(:short_id => m[1])
Query(Message)
.where("short_id = ?")
# Q 2468 : # message = Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2469 : # Message.where(:short_id => m[1]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2470 : # if hat.doffed_at?
#   
#   
#   time_ago_in_words_label(hat.doffed_at)
# end
Query(Hat)

# Q 2471 : # hat.doffed_at?
Query(Hat)

# Q 2472 : # story.user_is_author?
Query(Story)

# Q 2473 : # @user.session_token
Query(User)
.select('session_token')
# Q 2474 : # @user.session_token
Query(User)
.select('session_token')
# Q 2475 : # @user.session_token
Query(User)
.select('session_token')
# Q 2476 : # comment.delete_for_user(@user, params[:reason])
Query(Comment)

# Q 2477 : # comment.delete_for_user
Query(Comment)

# Q 2478 : # comment.delete_for_user
Query(Comment)

# Q 2479 : # hat.doffed_at
Query(Hat)
.select('doffed_at')
# Q 2480 : # self.results.order!
Query(Search)

# Q 2481 : # self.results
Query(Search)

# Q 2482 : # self.results.order!
Query(Search)

# Q 2483 : # self.results
Query(Search)

# Q 2484 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2485 : # @user.id
Query(User)

# Q 2486 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2487 : # @user.id
Query(User)

# Q 2488 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2489 : # @user.id
Query(User)

# Q 2490 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2491 : # @user.id
Query(User)

# Q 2492 : # message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2493 : # @user.id
Query(User)

# Q 2494 : # @user.username
Query(User)
.select('username')
# Q 2495 : # @user.username
Query(User)
.select('username')
# Q 2496 : # @user.username
Query(User)
.select('username')
# Q 2497 : # @user.username
Query(User)
.select('username')
# Q 2498 : # @user.username
Query(User)
.select('username')
# Q 2499 : # Story.votes_cast_type
Query(Story)

# Q 2500 : # Story.votes_cast_type
Query(Story)

# Q 2501 : # comment.downvotes
Query(Comment)
.select('downvotes')
# Q 2502 : # Story.votes_cast_type
Query(Story)

# Q 2503 : # Story.votes_cast_type
Query(Story)

# Q 2504 : # self.results.order!
Query(Search)

# Q 2505 : # self.results
Query(Search)

# Q 2506 : # Story.score_sql
Query(Story)

# Q 2507 : # self.results.order!
Query(Search)

# Q 2508 : # self.results
Query(Search)

# Q 2509 : # Story.score_sql
Query(Story)

# Q 2510 : # User.where(:password_reset_token => params[:token].to_s).first
Query(User)
.where("password_reset_token = ?")
.return_limit('1')
# Q 2511 : # User.where(:password_reset_token => params[:token].to_s).first
Query(User)
.where("password_reset_token = ?")
.return_limit('1')
# Q 2512 : # User.where(:password_reset_token => params[:token].to_s)
Query(User)
.where("password_reset_token = ?")
# Q 2513 : # User.where(:password_reset_token => params[:token].to_s).first
Query(User)
.where("password_reset_token = ?")
.return_limit('1')
# Q 2514 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2515 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2516 : # InvitationRequest.where(:code => params[:code].to_s)
Query(InvitationRequest)
.where("code = ?")
# Q 2517 : # InvitationRequest.where(:code => params[:code].to_s).first
Query(InvitationRequest)
.where("code = ?")
.return_limit('1')
# Q 2518 : # comment.showing_downvotes_for_user?
Query(Comment)

# Q 2519 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2520 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2521 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2522 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2523 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2524 : # Comment.find(v.comment_id)
Query(Comment)
.where("id = ?")
# Q 2525 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2526 : # Comment.find
Query(Comment)
.where("id = ?")
# Q 2527 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"])
Query(Story)

# Q 2528 : # Story.make!
Query(Story)

# Q 2529 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"])
Query(Story)

# Q 2530 : # Story.make!
Query(Story)

# Q 2531 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"])
Query(Story)

# Q 2532 : # Story.make!
Query(Story)

# Q 2533 : # Story.make!
Query(Story)

# Q 2534 : # comment.user_id
Query(Comment)
.select('user_id')
# Q 2535 : # @user.try
Query(User)

# Q 2536 : # @user.try
Query(User)

# Q 2537 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2538 : # story.user
Query(User)
.where("id = ?")
# Q 2539 : # Story.arel_table
Query(Story)

# Q 2540 : # Story.arel_table
Query(Story)

# Q 2541 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2542 : # @user.id
Query(User)

# Q 2543 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2544 : # @user.id
Query(User)

# Q 2545 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2546 : # @user.id
Query(User)

# Q 2547 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2548 : # @user.id
Query(User)

# Q 2549 : # message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2550 : # @user.id
Query(User)

# Q 2551 : # comment.vote_summary_for_user(@user).downcase
Query(Comment)

# Q 2552 : # comment.vote_summary_for_user
Query(Comment)

# Q 2553 : # story.html_class_for_user
Query(Story)

# Q 2554 : # story.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 2555 : # story.user
Query(User)
.where("id = ?")
# Q 2556 : # @user.is_moderator?
Query(User)

# Q 2557 : # @user.is_moderator?
Query(User)

# Q 2558 : # comment.current_vote
Query(Comment)

# Q 2559 : # comment.current_vote
Query(Comment)

# Q 2560 : # Comment.active.where("MATCH(comment) AGAINST('#{
# qwords}' IN BOOLEAN MODE)").includes(:user, :story)
Query(Comment)
.where("comment = ?")
.includes('user')
.includes('story')
# Q 2561 : # Comment.active.where("MATCH(comment) AGAINST('#{
# qwords}' IN BOOLEAN MODE)").includes(:user, :story)
Query(Comment)
.where("comment = ?")
.includes('user')
.includes('story')
# Q 2562 : # Comment.active.where("MATCH(comment) AGAINST('#{
# qwords}' IN BOOLEAN MODE)").includes
Query(Comment)
.where("comment = ?")
# Q 2563 : # Comment.active.where("MATCH(comment) AGAINST('#{
# qwords}' IN BOOLEAN MODE)")
Query(Comment)
.where("comment = ?")
# Q 2564 : # Comment.active.where
Query(Comment)

# Q 2565 : # Comment.active
Query(Comment)

# Q 2566 : # Comment.active.where("MATCH(comment) AGAINST('#{
# qwords}' IN BOOLEAN MODE)").includes
Query(Comment)
.where("comment = ?")
# Q 2567 : # Comment.active.where
Query(Comment)

# Q 2568 : # Comment.active
Query(Comment)

# Q 2569 : # comment.is_undeletable_by_user?(@user)
Query(Comment)

# Q 2570 : # comment.is_undeletable_by_user?
Query(Comment)

# Q 2571 : # comment.is_undeletable_by_user?
Query(Comment)

# Q 2572 : # story.created_at
Query(Story)
.select('created_at')
# Q 2573 : # Story.where(short_id: params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 2574 : # Story.where(short_id: params[:id])
Query(Story)
.where("short_id = ?")
# Q 2575 : # Story.where(short_id: params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 2576 : # comment.current_vote
Query(Comment)

# Q 2577 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2578 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2579 : # story.is_editable_by_user?
Query(Story)

# Q 2580 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2581 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2582 : # @story.title
Query(Story)
.select('title')
# Q 2583 : # @story.title
Query(Story)
.select('title')
# Q 2584 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2585 : # @user.id
Query(User)

# Q 2586 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2587 : # @user.id
Query(User)

# Q 2588 : # @story.merged_into_story.comments_path
Query(Story)
.where("id = ?")
# Q 2589 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2590 : # @story.merged_into_story.comments_path
Query(Story)
.where("id = ?")
# Q 2591 : # @story.merged_into_story
Query(Story)
.where("id = ?")
# Q 2592 : # message.save!
Query(Message)

# Q 2593 : # message.save!
Query(Message)

# Q 2594 : # message.save!
Query(Message)

# Q 2595 : # message.save!
Query(Message)

# Q 2596 : # message.save!
Query(Message)

# Q 2597 : # message.save!
Query(Message)

# Q 2598 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2599 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2600 : # User.where(:username => params[:user])
Query(User)
.where("username = ?")
# Q 2601 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 2602 : # comment.undelete_for_user(@user)
Query(Comment)

# Q 2603 : # comment.undelete_for_user
Query(Comment)

# Q 2604 : # comment.undelete_for_user
Query(Comment)

# Q 2605 : # User.make!(:username => "mod", :is_moderator => true)
Query(User)

# Q 2606 : # User.make!
Query(User)

# Q 2607 : # User.make!(:username => "mod", :is_moderator => true)
Query(User)

# Q 2608 : # User.make!
Query(User)

# Q 2609 : # User.make!(:username => "mod", :is_moderator => true)
Query(User)

# Q 2610 : # User.make!
Query(User)

# Q 2611 : # User.make!
Query(User)

# Q 2612 : # story.short_id
Query(Story)
.select('short_id')
# Q 2613 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2614 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2615 : # Story.find
Query(Story)
.where("id = ?")
# Q 2616 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2617 : # Story.find
Query(Story)
.where("id = ?")
# Q 2618 : # Story.find(v.story_id)
Query(Story)
.where("id = ?")
# Q 2619 : # Story.find
Query(Story)
.where("id = ?")
# Q 2620 : # Story.find
Query(Story)
.where("id = ?")
# Q 2621 : # @user.id
Query(User)

# Q 2622 : # @user.id
Query(User)

# Q 2623 : # story.has_suggestions?
Query(Story)

# Q 2624 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2625 : # HiddenStory.arel_table
Query(HiddenStory)

# Q 2626 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"], :description => "desc")
Query(Story)

# Q 2627 : # Story.make!
Query(Story)

# Q 2628 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"], :description => "desc")
Query(Story)

# Q 2629 : # Story.make!
Query(Story)

# Q 2630 : # Story.make!(:title => "blah", :tags_a => ["tag1", "tag2"], :description => "desc")
Query(Story)

# Q 2631 : # Story.make!
Query(Story)

# Q 2632 : # Story.make!
Query(Story)

# Q 2633 : # @story.can_be_seen_by_user?(@user)
Query(Story)

# Q 2634 : # @story.can_be_seen_by_user?
Query(Story)

# Q 2635 : # @story.can_be_seen_by_user?
Query(Story)

# Q 2636 : # stories.newest_by_user(by_user)
Query(Story)

# Q 2637 : # stories.newest_by_user
Query(Story)

# Q 2638 : # stories.newest_by_user
Query(Story)

# Q 2639 : # comment.is_gone?
Query(Comment)

# Q 2640 : # story.can_have_suggestions_from_user?
Query(Story)

# Q 2641 : # story.short_id
Query(Story)
.select('short_id')
# Q 2642 : # self.is_admin?
Query(User)

# Q 2643 : # self.is_admin?
Query(User)

# Q 2644 : # self.order
Query(Search)

# Q 2645 : # self.order
Query(Search)

# Q 2646 : # self.is_gone?
Query(Comment)

# Q 2647 : # self.gone_text
Query(Comment)

# Q 2648 : # self.is_gone?
Query(Comment)

# Q 2649 : # self.gone_text
Query(Comment)

# Q 2650 : # comment.gone_text
Query(Comment)

# Q 2651 : # @user.is_moderator?
Query(User)

# Q 2652 : # self.results.order!
Query(Search)

# Q 2653 : # self.results
Query(Search)

# Q 2654 : # self.results.order!
Query(Search)

# Q 2655 : # self.results
Query(Search)

# Q 2656 : # @story.title
Query(Story)
.select('title')
# Q 2657 : # @story.title
Query(Story)
.select('title')
# Q 2658 : # @story.title
Query(Story)
.select('title')
# Q 2659 : # comment.is_editable_by_user?(@user)
Query(Comment)

# Q 2660 : # comment.is_editable_by_user?
Query(Comment)

# Q 2661 : # comment.is_editable_by_user?
Query(Comment)

# Q 2662 : # story.is_gone?
Query(Story)

# Q 2663 : # Story.score_sql
Query(Story)

# Q 2664 : # Story.score_sql
Query(Story)

# Q 2665 : # @story.short_id_url
Query(Story)

# Q 2666 : # @story.short_id_url
Query(Story)

# Q 2667 : # @story.short_id_url
Query(Story)

# Q 2668 : # story.vote
Query(Story)

# Q 2669 : # story.vote
Query(Story)

# Q 2670 : # self.results.order!
Query(Search)

# Q 2671 : # self.results
Query(Search)

# Q 2672 : # self.results.order!
Query(Search)

# Q 2673 : # self.results
Query(Search)

# Q 2674 : # @user.update_unread_message_count!
Query(User)

# Q 2675 : # @user.update_unread_message_count!
Query(User)

# Q 2676 : # @user.is_moderator?
Query(User)

# Q 2677 : # @story.merged_comments.includes(:user, :story, :hat, :votes => :user).arrange_for_user(@user)
Query(Vote)
.includes('user')
.includes('votes')
.includes('user')
# Q 2678 : # @story.merged_comments.includes(:user, :story, :hat, :votes => :user).arrange_for_user(@user)
Query(Vote)
.includes('user')
.includes('votes')
.includes('user')
# Q 2679 : # @story.merged_comments.includes(:user, :story, :hat, :votes => :user).arrange_for_user
Query(Vote)
.includes('user')
.includes('votes')
.includes('user')
# Q 2680 : # @story.merged_comments.includes(:user, :story, :hat, :votes => :user)
Query(Vote)
.includes('user')
.includes('votes')
.includes('user')
# Q 2681 : # @story.merged_comments.includes
Query(Story)

# Q 2682 : # @story.merged_comments
Query(Story)

# Q 2683 : # @story.merged_comments.includes(:user, :story, :hat, :votes => :user).arrange_for_user
Query(Vote)
.includes('user')
.includes('votes')
.includes('user')
# Q 2684 : # @story.merged_comments.includes
Query(Story)

# Q 2685 : # @story.merged_comments
Query(Story)

# Q 2686 : # comment.markeddown_comment
Query(Comment)
.select('markeddown_comment')
# Q 2687 : # story.vote
Query(Story)

# Q 2688 : # self.results.order!
Query(Search)

# Q 2689 : # self.results
Query(Search)

# Q 2690 : # Comment.score_sql
Query(Comment)

# Q 2691 : # self.results.order!
Query(Search)

# Q 2692 : # self.results
Query(Search)

# Q 2693 : # Comment.score_sql
Query(Comment)

# Q 2694 : # @user.can_downvote?
Query(User)

# Q 2695 : # self.avatar_url
Query(User)

# Q 2696 : # self.avatar_url
Query(User)

# Q 2697 : # self.avatar_url
Query(User)

# Q 2698 : # SavedStory.arel_table
Query(SavedStory)

# Q 2699 : # SavedStory.arel_table
Query(SavedStory)

# Q 2700 : # @user.wearable_hats.where(:id => params[:hat_id])
Query(Hat)
.where("user_id = ?")
.where("id = ?")
# Q 2701 : # @user.wearable_hats.where
Query(Hat)
.where("user_id = ?")
# Q 2702 : # @user.wearable_hats
Query(Hat)
.where("user_id = ?")
# Q 2703 : # @user.wearable_hats.where
Query(Hat)
.where("user_id = ?")
# Q 2704 : # @user.wearable_hats
Query(Hat)
.where("user_id = ?")
# Q 2705 : # Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2706 : # mod_log = Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2707 : # mod_log = Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2708 : # Moderation.last
Query(Moderation)
.return_limit('1')
# Q 2709 : # comment.markeddown_comment
Query(Comment)
.select('markeddown_comment')
# Q 2710 : # SavedStory.arel_table
Query(SavedStory)

# Q 2711 : # @user.id
Query(User)

# Q 2712 : # SavedStory.arel_table
Query(SavedStory)

# Q 2713 : # @user.id
Query(User)

# Q 2714 : # story.is_hidden_by_cur_user
Query(Story)

# Q 2715 : # self.send(k)
Query(Comment)

# Q 2716 : # self.send(k)
Query(Comment)

# Q 2717 : # self.send
Query(Comment)

# Q 2718 : # self.send(k)
Query(Comment)

# Q 2719 : # self.send
Query(Comment)

# Q 2720 : # self.send(k)
Query(Comment)

# Q 2721 : # self.send
Query(Comment)

# Q 2722 : # self.send
Query(Comment)

# Q 2723 : # self.github_username.present?
Query(User)

# Q 2724 : # self.github_username
Query(User)

# Q 2725 : # self.github_username.present?
Query(User)

# Q 2726 : # self.github_username
Query(User)

# Q 2727 : # @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2728 : # @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2729 : # @story.comments
Query(Comment)
.where("story_id = ?")
# Q 2730 : # @comment = @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2731 : # @story.comments.build
Query(Comment)
.where("story_id = ?")
# Q 2732 : # @story.comments
Query(Comment)
.where("story_id = ?")
# Q 2733 : # Tag.where(:tag => cookies[TAG_FILTER_COOKIE].to_s.split(","))
Query(Tag)
.where("tag = ?")
# Q 2734 : # story.short_id
Query(Story)
.select('short_id')
# Q 2735 : # self.github_username
Query(User)

# Q 2736 : # self.github_username
Query(User)

# Q 2737 : # self.github_username
Query(User)

# Q 2738 : # SavedStory.arel_table
Query(SavedStory)

# Q 2739 : # SavedStory.arel_table
Query(SavedStory)

# Q 2740 : # @message.save
Query(Message)

# Q 2741 : # @message.save
Query(Message)

# Q 2742 : # self.page
Query(Search)

# Q 2743 : # self.page_count
Query(Search)

# Q 2744 : # self.page
Query(Search)

# Q 2745 : # self.page_count
Query(Search)

# Q 2746 : # comment.save
Query(Comment)

# Q 2747 : # comment.save
Query(Comment)

# Q 2748 : # self.send(k.values.first)
Query(Comment)

# Q 2749 : # self.send(k.values.first)
Query(Comment)

# Q 2750 : # self.send
Query(Comment)

# Q 2751 : # self.send(k.values.first)
Query(Comment)

# Q 2752 : # self.send
Query(Comment)

# Q 2753 : # self.send(k.values.first)
Query(Comment)

# Q 2754 : # self.send
Query(Comment)

# Q 2755 : # self.send(k.values.first)
Query(Comment)

# Q 2756 : # self.send
Query(Comment)

# Q 2757 : # self.send
Query(Comment)

# Q 2758 : # self.page_count
Query(Search)

# Q 2759 : # self.page_count
Query(Search)

# Q 2760 : # self.page_count
Query(Search)

# Q 2761 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, [comment.id])
Query(Vote)

# Q 2762 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, [comment.id])
Query(Vote)

# Q 2763 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2764 : # @user.id
Query(User)

# Q 2765 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2766 : # @user.id
Query(User)

# Q 2767 : # story.short_id
Query(Story)
.select('short_id')
# Q 2768 : # self.twitter_username.present?
Query(User)

# Q 2769 : # self.twitter_username
Query(User)

# Q 2770 : # self.twitter_username.present?
Query(User)

# Q 2771 : # self.twitter_username
Query(User)

# Q 2772 : # Story.where(:url => urls).where("is_expired = ? OR is_moderated = ?", false, true).order("id DESC").first
Query(Story)
.where("url = ?")
.where(" = ?")
.order('id')
.order('id')
.return_limit('1')
# Q 2773 : # Story.where(:url => urls).where("is_expired = ? OR is_moderated = ?", false, true).order("id DESC")
Query(Story)
.where("url = ?")
.where(" = ?")
.order('id')
.order('id')
# Q 2774 : # Story.where(:url => urls).where("is_expired = ? OR is_moderated = ?", false, true).order
Query(Story)
.where("url = ?")
.where(" = ?")
# Q 2775 : # Story.where(:url => urls).where("is_expired = ? OR is_moderated = ?", false, true)
Query(Story)
.where("url = ?")
.where(" = ?")
# Q 2776 : # Story.where(:url => urls).where
Query(Story)
.where("url = ?")
# Q 2777 : # Story.where(:url => urls)
Query(Story)
.where("url = ?")
# Q 2778 : # Story.where(:url => urls).where("is_expired = ? OR is_moderated = ?", false, true).order("id DESC").first
Query(Story)
.where("url = ?")
.where(" = ?")
.order('id')
.order('id')
.return_limit('1')
# Q 2779 : # Story.where(:url => urls).where("is_expired = ? OR is_moderated = ?", false, true).order
Query(Story)
.where("url = ?")
.where(" = ?")
# Q 2780 : # Story.where(:url => urls).where
Query(Story)
.where("url = ?")
# Q 2781 : # comment.id
Query(Comment)

# Q 2782 : # comment.id
Query(Comment)

# Q 2783 : # self.twitter_username
Query(User)

# Q 2784 : # self.twitter_username
Query(User)

# Q 2785 : # self.twitter_username
Query(User)

# Q 2786 : # self.page
Query(Search)

# Q 2787 : # self.page
Query(Search)

# Q 2788 : # @story.title
Query(Story)
.select('title')
# Q 2789 : # @story.title
Query(Story)
.select('title')
# Q 2790 : # @story.title
Query(Story)
.select('title')
# Q 2791 : # comment.id
Query(Comment)

# Q 2792 : # comment.id
Query(Comment)

# Q 2793 : # @user.id
Query(User)

# Q 2794 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2795 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2796 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2797 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2798 : # story.hider_count
Query(Story)

# Q 2799 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2800 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2801 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2802 : # @story.comments_count
Query(Story)
.select('comments_count')
# Q 2803 : # story.hider_count
Query(Story)

# Q 2804 : # Story.arel_table
Query(Story)

# Q 2805 : # Story.arel_table
Query(Story)

# Q 2806 : # self.results.limit(self.per_page).offset((
# self.page - 1) * self.per_page)
Query(Search)
.return_limit('')
# Q 2807 : # self.results.limit(self.per_page).offset((
# self.page - 1) * self.per_page)
Query(Search)
.return_limit('')
# Q 2808 : # self.results.limit(self.per_page).offset
Query(Search)
.return_limit('')
# Q 2809 : # self.results.limit(self.per_page)
Query(Search)
.return_limit('')
# Q 2810 : # self.results.limit
Query(Search)
.return_limit('')
# Q 2811 : # self.results
Query(Search)

# Q 2812 : # self.results.limit(self.per_page).offset
Query(Search)
.return_limit('')
# Q 2813 : # self.results.limit
Query(Search)
.return_limit('')
# Q 2814 : # self.results
Query(Search)

# Q 2815 : # Tagging.arel_table
Query(Tagging)

# Q 2816 : # Tagging.arel_table
Query(Tagging)

# Q 2817 : # stories.recent
Query(Story)

# Q 2818 : # stories.recent
Query(Story)

# Q 2819 : # story.is_saved_by_cur_user
Query(Story)

# Q 2820 : # self.per_page
Query(Search)

# Q 2821 : # self.per_page
Query(Search)

# Q 2822 : # Tagging.arel_table
Query(Tagging)

# Q 2823 : # Tagging.arel_table
Query(Tagging)

# Q 2824 : # story.short_id
Query(Story)
.select('short_id')
# Q 2825 : # self.page
Query(Search)

# Q 2826 : # self.per_page
Query(Search)

# Q 2827 : # self.page
Query(Search)

# Q 2828 : # self.per_page
Query(Search)

# Q 2829 : # stories.newest
Query(Story)

# Q 2830 : # stories.newest
Query(Story)

# Q 2831 : # self.totp_secret
Query(User)

# Q 2832 : # self.totp_secret
Query(User)

# Q 2833 : # Story.order("id DESC").limit(100).each
Query(Story)
.order('id')
.order('id')
.return_limit('')
# Q 2834 : # Story.order("id DESC").limit(100)
Query(Story)
.order('id')
.order('id')
.return_limit('')
# Q 2835 : # Story.order("id DESC").limit
Query(Story)
.order('id')
.order('id')
.return_limit('')
# Q 2836 : # Story.order("id DESC")
Query(Story)
.order('id')
.order('id')
# Q 2837 : # Story.order
Query(Story)

# Q 2838 : # Story.order("id DESC").limit(100).each
Query(Story)
.order('id')
.order('id')
.return_limit('')
# Q 2839 : # Story.order("id DESC").limit
Query(Story)
.order('id')
.order('id')
.return_limit('')
# Q 2840 : # Story.order
Query(Story)

# Q 2841 : # Tagging.arel_table
Query(Tagging)

# Q 2842 : # Tagging.arel_table
Query(Tagging)

# Q 2843 : # @story.user.twitter_username.present?
Query(User)
.where("id = ?")
# Q 2844 : # @story.user.twitter_username
Query(User)
.where("id = ?")
# Q 2845 : # @story.user
Query(User)
.where("id = ?")
# Q 2846 : # if @story.user.twitter_username.present?
#   
#   @meta_tags["twitter:creator"] = "@" + @story.user.twitter_username
# end
Query(Story)

# Q 2847 : # @story.user.twitter_username.present?
Query(User)
.where("id = ?")
# Q 2848 : # @story.user.twitter_username
Query(User)
.where("id = ?")
# Q 2849 : # @story.user
Query(User)
.where("id = ?")
# Q 2850 : # User.where(:rss_token => params[:token].to_s).first
Query(User)
.where("rss_token = ?")
.return_limit('1')
# Q 2851 : # User.where(:rss_token => params[:token].to_s).first
Query(User)
.where("rss_token = ?")
.return_limit('1')
# Q 2852 : # User.where(:rss_token => params[:token].to_s)
Query(User)
.where("rss_token = ?")
# Q 2853 : # User.where(:rss_token => params[:token].to_s).first
Query(User)
.where("rss_token = ?")
.return_limit('1')
# Q 2854 : # @story.user.twitter_username
Query(User)
.where("id = ?")
# Q 2855 : # @story.user
Query(User)
.where("id = ?")
# Q 2856 : # @story.user.twitter_username
Query(User)
.where("id = ?")
# Q 2857 : # @story.user
Query(User)
.where("id = ?")
# Q 2858 : # @story.user.twitter_username
Query(User)
.where("id = ?")
# Q 2859 : # @story.user
Query(User)
.where("id = ?")
# Q 2860 : # story.short_id
Query(Story)
.select('short_id')
# Q 2861 : # self.calculated_confidence
Query(Comment)

# Q 2862 : # self.calculated_confidence
Query(Comment)

# Q 2863 : # self.calculated_confidence
Query(Comment)

# Q 2864 : # Story.find_each
Query(Story)

# Q 2865 : # Story.find_each
Query(Story)

# Q 2866 : # Message.where(:short_id => params[:message_id] || params[:id]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2867 : # Message.where(:short_id => params[:message_id] || params[:id]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2868 : # Message.where(:short_id => params[:message_id] || params[:id])
Query(Message)
.where("short_id = ?")
# Q 2869 : # Message.where(:short_id => params[:message_id] || params[:id]).first
Query(Message)
.where("short_id = ?")
.return_limit('1')
# Q 2870 : # @user.is_moderator?
Query(User)

# Q 2871 : # self.username
Query(User)
.select('username')
# Q 2872 : # self.username
Query(User)
.select('username')
# Q 2873 : # Vote.story_votes_by_user_for_story_ids_hash(user.id, self.results.map { |s|
#   
#   s.id
# })
Query(Vote)

# Q 2874 : # Vote.story_votes_by_user_for_story_ids_hash(user.id, self.results.map { |s|
#   
#   s.id
# })
Query(Vote)

# Q 2875 : # Vote.story_votes_by_user_for_story_ids_hash
Query(Vote)

# Q 2876 : # user.id
Query(User)

# Q 2877 : # Vote.story_votes_by_user_for_story_ids_hash
Query(Vote)

# Q 2878 : # user.id
Query(User)

# Q 2879 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2880 : # @user.id
Query(User)

# Q 2881 : # @message.author_user_id
Query(Message)
.select('author_user_id')
# Q 2882 : # @user.id
Query(User)

# Q 2883 : # story.url.present?
Query(Story)
.select('url')
# Q 2884 : # story.url
Query(Story)
.select('url')
# Q 2885 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2886 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2887 : # ShortId.new(self.class)
Query(ShortId)

# Q 2888 : # ShortId.new
Query(ShortId)

# Q 2889 : # self.class
Query(Comment)

# Q 2890 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 2891 : # ShortId.new
Query(ShortId)

# Q 2892 : # self.class
Query(Comment)

# Q 2893 : # self.results.map
Query(Search)

# Q 2894 : # self.results
Query(Search)

# Q 2895 : # self.results.map
Query(Search)

# Q 2896 : # self.results
Query(Search)

# Q 2897 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2898 : # @user.id
Query(User)

# Q 2899 : # @message.recipient_user_id
Query(Message)
.select('recipient_user_id')
# Q 2900 : # @user.id
Query(User)

# Q 2901 : # @user.save!
Query(User)

# Q 2902 : # @user.save!
Query(User)

# Q 2903 : # story.archive_url
Query(Story)

# Q 2904 : # self.results.each
Query(Search)

# Q 2905 : # self.results
Query(Search)

# Q 2906 : # self.results.each
Query(Search)

# Q 2907 : # self.results
Query(Search)

# Q 2908 : # self.karma
Query(User)
.select('karma')
# Q 2909 : # self.karma
Query(User)
.select('karma')
# Q 2910 : # self.karma
Query(User)
.select('karma')
# Q 2911 : # @story.as_json(:with_comments => @comments)
Query(Story)

# Q 2912 : # @story.as_json
Query(Story)

# Q 2913 : # @story.as_json(:with_comments => @comments)
Query(Story)

# Q 2914 : # @story.as_json
Query(Story)

# Q 2915 : # @story.as_json
Query(Story)

# Q 2916 : # @user.pushover_user_key.present?
Query(User)

# Q 2917 : # @user.pushover_user_key
Query(User)

# Q 2918 : # @user.pushover_user_key.present?
Query(User)

# Q 2919 : # @user.pushover_user_key
Query(User)

# Q 2920 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, comment.story_id, comment.id, @user.id, nil)
Query(Vote)

# Q 2921 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2922 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2923 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2924 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2925 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2926 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 2927 : # comment.id
Query(Comment)

# Q 2928 : # @user.id
Query(User)

# Q 2929 : # comment.id
Query(Comment)

# Q 2930 : # @user.id
Query(User)

# Q 2931 : # story.is_gone?
Query(Story)

# Q 2932 : # self.parent_comment_id.present?
Query(Comment)
.select('parent_comment_id')
# Q 2933 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 2934 : # self.parent_comment_id.present?
Query(Comment)
.select('parent_comment_id')
# Q 2935 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 2936 : # self.parent_comment.thread_id
Query(Comment)
.where("id = ?")
.select('thread_id')
# Q 2937 : # self.parent_comment.thread_id
Query(Comment)
.where("id = ?")
.select('thread_id')
# Q 2938 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 2939 : # self.parent_comment.thread_id
Query(Comment)
.where("id = ?")
.select('thread_id')
# Q 2940 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 2941 : # self.stories_submitted_count
Query(User)

# Q 2942 : # self.comments_posted_count
Query(User)

# Q 2943 : # self.stories_submitted_count
Query(User)

# Q 2944 : # self.comments_posted_count
Query(User)

# Q 2945 : # story.comments_path
Query(Story)

# Q 2946 : # Keystore.incremented_value_for("thread_id")
Query(Keystore)

# Q 2947 : # Keystore.incremented_value_for("thread_id")
Query(Keystore)

# Q 2948 : # Keystore.incremented_value_for
Query(Keystore)

# Q 2949 : # Keystore.incremented_value_for
Query(Keystore)

# Q 2950 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2951 : # Story.connection.adapter_name.match(/mysql/i)
Query(Story)

# Q 2952 : # Story.connection.adapter_name.match
Query(Story)

# Q 2953 : # Story.connection.adapter_name
Query(Story)

# Q 2954 : # Story.connection
Query(Story)

# Q 2955 : # Story.connection.adapter_name.match
Query(Story)

# Q 2956 : # Story.connection.adapter_name
Query(Story)

# Q 2957 : # Story.connection
Query(Story)

# Q 2958 : # Vote.comment_votes_by_user_for_comment_ids_hash(user.id, self.results.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 2959 : # Vote.comment_votes_by_user_for_comment_ids_hash(user.id, self.results.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 2960 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2961 : # user.id
Query(User)

# Q 2962 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 2963 : # user.id
Query(User)

# Q 2964 : # @story.can_have_suggestions_from_user?(@user)
Query(Story)

# Q 2965 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 2966 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 2967 : # self.results.map
Query(Search)

# Q 2968 : # self.results
Query(Search)

# Q 2969 : # self.results.map
Query(Search)

# Q 2970 : # self.results
Query(Search)

# Q 2971 : # User.transaction
Query(User)

# Q 2972 : # User.transaction
Query(User)

# Q 2973 : # @story.comments_path
Query(Story)

# Q 2974 : # @story.comments_path
Query(Story)

# Q 2975 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2976 : # self.results.each
Query(Search)

# Q 2977 : # self.results
Query(Search)

# Q 2978 : # self.results.each
Query(Search)

# Q 2979 : # self.results
Query(Search)

# Q 2980 : # stories.saved
Query(Story)

# Q 2981 : # stories.saved
Query(Story)

# Q 2982 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 2983 : # self.url
Query(Story)
.select('url')
# Q 2984 : # self.url
Query(Story)
.select('url')
# Q 2985 : # @story.suggested_taggings.where(:user_id => @user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 2986 : # @story.suggested_taggings.where(:user_id => @user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 2987 : # @story.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2988 : # @story.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2989 : # @user.id
Query(User)

# Q 2990 : # @story.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2991 : # @story.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 2992 : # @user.id
Query(User)

# Q 2993 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, comment.story_id, comment.id, @user.id, params[:reason])
Query(Vote)

# Q 2994 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2995 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2996 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 2997 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 2998 : # self.save!
Query(User)

# Q 2999 : # self.save!
Query(User)

# Q 3000 : # self.save!
Query(User)

# Q 3001 : # comment.id
Query(Comment)

# Q 3002 : # @user.id
Query(User)

# Q 3003 : # comment.id
Query(Comment)

# Q 3004 : # @user.id
Query(User)

# Q 3005 : # Message.new
Query(Message)

# Q 3006 : # Message.new
Query(Message)

# Q 3007 : # msg = Message.new
Query(Message)

# Q 3008 : # Message.new
Query(Message)

# Q 3009 : # @story.suggested_titles.where(:user_id => @user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 3010 : # @story.suggested_titles.where(:user_id => @user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 3011 : # @story.suggested_titles.where(:user_id => @user.id)
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
# Q 3012 : # @story.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3013 : # @story.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3014 : # @user.id
Query(User)

# Q 3015 : # @story.suggested_titles.where(:user_id => @user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 3016 : # @story.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3017 : # @story.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3018 : # @user.id
Query(User)

# Q 3019 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 3020 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 3021 : # @user.is_admin?
Query(User)

# Q 3022 : # User.where(:session_token => session[:twofa_u]).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 3023 : # User.where(:session_token => session[:twofa_u])
Query(User)
.where("session_token = ?")
# Q 3024 : # User.where(:session_token => session[:twofa_u]).first
Query(User)
.where("session_token = ?")
.return_limit('1')
# Q 3025 : # story.downvotes
Query(Story)
.select('downvotes')
# Q 3026 : # @user.is_moderator?
Query(User)

# Q 3027 : # self.id
Query(User)

# Q 3028 : # self.id
Query(User)

# Q 3029 : # self.id
Query(User)

# Q 3030 : # story.downvotes
Query(Story)
.select('downvotes')
# Q 3031 : # story.score
Query(Story)

# Q 3032 : # story.vote_summary_for(@user).downcase
Query(Story)

# Q 3033 : # story.vote_summary_for
Query(Story)

# Q 3034 : # @story.can_have_suggestions_from_user?(@user)
Query(Story)

# Q 3035 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 3036 : # @story.can_have_suggestions_from_user?
Query(Story)

# Q 3037 : # @story.comments_path
Query(Story)

# Q 3038 : # @story.comments_path
Query(Story)

# Q 3039 : # @user.username
Query(User)
.select('username')
# Q 3040 : # @user.username
Query(User)
.select('username')
# Q 3041 : # @user.username
Query(User)
.select('username')
# Q 3042 : # @user.username
Query(User)
.select('username')
# Q 3043 : # @user.username
Query(User)
.select('username')
# Q 3044 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 3045 : # @story.dup
Query(Story)

# Q 3046 : # @story.dup
Query(Story)

# Q 3047 : # @story.dup
Query(Story)

# Q 3048 : # Moderation.new
Query(Moderation)

# Q 3049 : # Moderation.new
Query(Moderation)

# Q 3050 : # m = Moderation.new
Query(Moderation)

# Q 3051 : # Moderation.new
Query(Moderation)

# Q 3052 : # @user.can_downvote?(comment)
Query(User)

# Q 3053 : # @user.can_downvote?
Query(User)

# Q 3054 : # @user.can_downvote?
Query(User)

# Q 3055 : # story.comments_path
Query(Story)

# Q 3056 : # story.comments_count
Query(Story)
.select('comments_count')
# Q 3057 : # self.tags.map { |t|
#   
#   t.tag
# }.sort
Query(Tag)
.where("story_id = ?")
# Q 3058 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 3059 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 3060 : # self.tags.map { |t|
#   
#   t.tag
# }.sort
Query(Tag)
.where("story_id = ?")
# Q 3061 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 3062 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 3063 : # self.id
Query(User)

# Q 3064 : # self.id
Query(User)

# Q 3065 : # self.id
Query(User)

# Q 3066 : # @story.valid?
Query(Story)

# Q 3067 : # @story.valid?
Query(Story)

# Q 3068 : # @user.save!
Query(User)

# Q 3069 : # @user.save!
Query(User)

# Q 3070 : # self.generated_markeddown_comment
Query(Comment)

# Q 3071 : # self.generated_markeddown_comment
Query(Comment)

# Q 3072 : # self.generated_markeddown_comment
Query(Comment)

# Q 3073 : # @story.title
Query(Story)
.select('title')
# Q 3074 : # @story.title
Query(Story)
.select('title')
# Q 3075 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, comment.story_id, comment.id, @user.id, params[:reason])
Query(Vote)

# Q 3076 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3077 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 3078 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3079 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 3080 : # @story.save_suggested_title_for_user!(@story.title, @user)
Query(Story)

# Q 3081 : # @story.save_suggested_title_for_user!
Query(Story)

# Q 3082 : # @story.title
Query(Story)
.select('title')
# Q 3083 : # @story.save_suggested_title_for_user!
Query(Story)

# Q 3084 : # @story.title
Query(Story)
.select('title')
# Q 3085 : # comment.id
Query(Comment)

# Q 3086 : # @user.id
Query(User)

# Q 3087 : # comment.id
Query(Comment)

# Q 3088 : # @user.id
Query(User)

# Q 3089 : # Tag.where(:tag => params[:tag]).first!
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3090 : # Tag.where(:tag => params[:tag]).first!
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3091 : # Tag.where(:tag => params[:tag])
Query(Tag)
.where("tag = ?")
# Q 3092 : # Tag.where(:tag => params[:tag]).first!
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 3093 : # @story.tags_a.sort
Query(Story)

# Q 3094 : # @story.tags_a
Query(Story)

# Q 3095 : # @story.tags_a.sort
Query(Story)

# Q 3096 : # @story.tags_a
Query(Story)

# Q 3097 : # user.is_moderator?
Query(User)

# Q 3098 : # user.id
Query(User)

# Q 3099 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3100 : # user.is_moderator?
Query(User)

# Q 3101 : # user.id
Query(User)

# Q 3102 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3103 : # self.send(k)
Query(Story)

# Q 3104 : # self.send(k)
Query(Story)

# Q 3105 : # self.send
Query(Story)

# Q 3106 : # self.send(k)
Query(Story)

# Q 3107 : # self.send
Query(Story)

# Q 3108 : # self.send(k)
Query(Story)

# Q 3109 : # self.send
Query(Story)

# Q 3110 : # self.send
Query(Story)

# Q 3111 : # @story.save_suggested_tags_a_for_user!(sugtags, @user)
Query(Story)

# Q 3112 : # @story.save_suggested_tags_a_for_user!
Query(Story)

# Q 3113 : # @story.save_suggested_tags_a_for_user!
Query(Story)

# Q 3114 : # User.transaction
Query(User)

# Q 3115 : # User.transaction
Query(User)

# Q 3116 : # stories.tagged(@tag)
Query(Story)

# Q 3117 : # stories.tagged
Query(Story)

# Q 3118 : # stories.tagged
Query(Story)

# Q 3119 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 3120 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 3121 : # Moderation.new
Query(Moderation)

# Q 3122 : # Moderation.new
Query(Moderation)

# Q 3123 : # Moderation.new
Query(Moderation)

# Q 3124 : # self.send(k.values.first)
Query(Story)

# Q 3125 : # self.send(k.values.first)
Query(Story)

# Q 3126 : # self.send
Query(Story)

# Q 3127 : # self.send(k.values.first)
Query(Story)

# Q 3128 : # self.send
Query(Story)

# Q 3129 : # self.send(k.values.first)
Query(Story)

# Q 3130 : # self.send
Query(Story)

# Q 3131 : # self.send(k.values.first)
Query(Story)

# Q 3132 : # self.send
Query(Story)

# Q 3133 : # self.send
Query(Story)

# Q 3134 : # @user.save!
Query(User)

# Q 3135 : # @user.save!
Query(User)

# Q 3136 : # self.id
Query(Comment)

# Q 3137 : # self.id
Query(Comment)

# Q 3138 : # self.id
Query(Comment)

# Q 3139 : # @tag.description.blank?
Query(Tag)
.select('description')
# Q 3140 : # @tag.description
Query(Tag)
.select('description')
# Q 3141 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3142 : # @tag.description
Query(Tag)
.select('description')
# Q 3143 : # @tag.description.blank?
Query(Tag)
.select('description')
# Q 3144 : # @tag.description
Query(Tag)
.select('description')
# Q 3145 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3146 : # @tag.description
Query(Tag)
.select('description')
# Q 3147 : # user.id
Query(User)

# Q 3148 : # user.id
Query(User)

# Q 3149 : # user.id
Query(User)

# Q 3150 : # @story.reload
Query(Story)

# Q 3151 : # @story.reload
Query(Story)

# Q 3152 : # @story.reload
Query(Story)

# Q 3153 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3154 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3155 : # self.delete!
Query(User)

# Q 3156 : # self.delete!
Query(User)

# Q 3157 : # self.delete!
Query(User)

# Q 3158 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3159 : # @tag.description
Query(Tag)
.select('description')
# Q 3160 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3161 : # @tag.description
Query(Tag)
.select('description')
# Q 3162 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3163 : # @tag.tag
Query(Tag)
.select('tag')
# Q 3164 : # Moderation.new
Query(Moderation)

# Q 3165 : # Moderation.new
Query(Moderation)

# Q 3166 : # m = Moderation.new
Query(Moderation)

# Q 3167 : # Moderation.new
Query(Moderation)

# Q 3168 : # self.id
Query(User)

# Q 3169 : # self.id
Query(User)

# Q 3170 : # self.id
Query(User)

# Q 3171 : # self.calculated_hotness
Query(Story)

# Q 3172 : # self.calculated_hotness
Query(Story)

# Q 3173 : # self.calculated_hotness
Query(Story)

# Q 3174 : # self.save(:validate => false)
Query(Comment)

# Q 3175 : # self.save
Query(Comment)

# Q 3176 : # self.save
Query(Comment)

# Q 3177 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 3178 : # @story.is_editable_by_user?
Query(Story)

# Q 3179 : # @story.is_editable_by_user?
Query(Story)

# Q 3180 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes(:user, :story)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
.return_limit('')
.includes('user')
.includes('story')
# Q 3181 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes(:user, :story)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
.return_limit('')
.includes('user')
.includes('story')
# Q 3182 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
.return_limit('')
# Q 3183 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
.return_limit('')
# Q 3184 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
.return_limit('')
# Q 3185 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
# Q 3186 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
# Q 3187 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC")
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
# Q 3188 : # Comment.where(:is_deleted => false, :is_moderated => false).order
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
# Q 3189 : # Comment.where(:is_deleted => false, :is_moderated => false)
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
# Q 3190 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit(COMMENTS_PER_PAGE).includes
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
.return_limit('')
# Q 3191 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset((
# @page - 1) * COMMENTS_PER_PAGE).limit
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
.return_limit('')
# Q 3192 : # Comment.where(:is_deleted => false, :is_moderated => false).order("id DESC").offset
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
.order('id')
.order('id')
# Q 3193 : # Comment.where(:is_deleted => false, :is_moderated => false).order
Query(Comment)
.where("is_deleted = ?")
.where("is_moderated = ?")
# Q 3194 : # @story.is_undeletable_by_user?(@user)
Query(Story)

# Q 3195 : # @story.is_undeletable_by_user?
Query(Story)

# Q 3196 : # @story.is_undeletable_by_user?
Query(Story)

# Q 3197 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3198 : # self.story
Query(Story)
.where("id = ?")
# Q 3199 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3200 : # self.story
Query(Story)
.where("id = ?")
# Q 3201 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 3202 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 3203 : # ShortId.new(self.class)
Query(ShortId)

# Q 3204 : # ShortId.new
Query(ShortId)

# Q 3205 : # self.class
Query(Story)

# Q 3206 : # ShortId.new(self.class).generate
Query(ShortId)

# Q 3207 : # ShortId.new
Query(ShortId)

# Q 3208 : # self.class
Query(Story)

# Q 3209 : # self.user.update_comments_posted_count!
Query(User)
.where("id = ?")
# Q 3210 : # self.user
Query(User)
.where("id = ?")
# Q 3211 : # self.user.update_comments_posted_count!
Query(User)
.where("id = ?")
# Q 3212 : # self.user
Query(User)
.where("id = ?")
# Q 3213 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq.each
Query(Comment)
.distinct('')
# Q 3214 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq
Query(Comment)
.distinct('')
# Q 3215 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten
Query(Comment)

# Q 3216 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/)
Query(Comment)

# Q 3217 : # self.plaintext_comment.scan
Query(Comment)

# Q 3218 : # self.plaintext_comment
Query(Comment)

# Q 3219 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq.each
Query(Comment)
.distinct('')
# Q 3220 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten.uniq
Query(Comment)
.distinct('')
# Q 3221 : # self.plaintext_comment.scan(/\B\@([\w\-]+)/).flatten
Query(Comment)

# Q 3222 : # self.plaintext_comment.scan
Query(Comment)

# Q 3223 : # self.plaintext_comment
Query(Comment)

# Q 3224 : # @story.save(:validate => false)
Query(Story)

# Q 3225 : # @story.save
Query(Story)

# Q 3226 : # @story.save
Query(Story)

# Q 3227 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3228 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3229 : # User.where(:username => mention)
Query(User)
.where("username = ?")
# Q 3230 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3231 : # User.where(:username => mention)
Query(User)
.where("username = ?")
# Q 3232 : # User.where(:username => mention).first
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3233 : # self.user.id
Query(User)
.where("id = ?")
# Q 3234 : # self.user
Query(User)
.where("id = ?")
# Q 3235 : # self.user.id
Query(User)
.where("id = ?")
# Q 3236 : # self.user
Query(User)
.where("id = ?")
# Q 3237 : # self.user.id
Query(User)
.where("id = ?")
# Q 3238 : # self.user
Query(User)
.where("id = ?")
# Q 3239 : # self.user.id
Query(User)
.where("id = ?")
# Q 3240 : # self.user
Query(User)
.where("id = ?")
# Q 3241 : # self.tags.map { |t|
#   
#   t.hotness_mod
# }.sum
Query(Tag)
.where("story_id = ?")
# Q 3242 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 3243 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 3244 : # self.user_is_author
Query(Story)
.select('user_is_author')
# Q 3245 : # self.tags.map { |t|
#   
#   t.hotness_mod
# }.sum
Query(Tag)
.where("story_id = ?")
# Q 3246 : # self.tags.map
Query(Tag)
.where("story_id = ?")
# Q 3247 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 3248 : # self.user_is_author
Query(Story)
.select('user_is_author')
# Q 3249 : # @story.comments_path
Query(Story)

# Q 3250 : # @story.comments_path
Query(Story)

# Q 3251 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   if base < 0
#     
#     c.downvotes * -0.5
#   else
#     
#     c.upvotes + 1 - c.downvotes
#   end
# }.inject(&:+).to_f
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3252 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   if base < 0
#     
#     c.downvotes * -0.5
#   else
#     
#     c.upvotes + 1 - c.downvotes
#   end
# }.inject(&:+)
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3253 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   if base < 0
#     
#     c.downvotes * -0.5
#   else
#     
#     c.upvotes + 1 - c.downvotes
#   end
# }.inject
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3254 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3255 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes)
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3256 : # self.comments.where("user_id <> ?", self.user_id).select
Query(Comment)
.where("story_id = ?")
.where(" = ?")
# Q 3257 : # self.comments.where("user_id <> ?", self.user_id)
Query(Comment)
.where("story_id = ?")
.where(" = ?")
# Q 3258 : # self.comments.where
Query(Comment)
.where("story_id = ?")
# Q 3259 : # self.comments
Query(Comment)
.where("story_id = ?")
# Q 3260 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   if base < 0
#     
#     c.downvotes * -0.5
#   else
#     
#     c.upvotes + 1 - c.downvotes
#   end
# }.inject(&:+).to_f
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3261 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map { |c|
#   
#   if base < 0
#     
#     c.downvotes * -0.5
#   else
#     
#     c.upvotes + 1 - c.downvotes
#   end
# }.inject
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3262 : # self.comments.where("user_id <> ?", self.user_id).select(:upvotes, :downvotes).map
Query(Comment)
.where("story_id = ?")
.where(" = ?")
.select('upvotes')
.select('downvotes')
# Q 3263 : # self.comments.where("user_id <> ?", self.user_id).select
Query(Comment)
.where("story_id = ?")
.where(" = ?")
# Q 3264 : # self.comments.where
Query(Comment)
.where("story_id = ?")
# Q 3265 : # self.comments
Query(Comment)
.where("story_id = ?")
# Q 3266 : # @user.save!
Query(User)

# Q 3267 : # @user.save!
Query(User)

# Q 3268 : # self.user_id
Query(Story)
.select('user_id')
# Q 3269 : # self.user_id
Query(Story)
.select('user_id')
# Q 3270 : # @story.is_editable_by_user?(@user)
Query(Story)

# Q 3271 : # @story.is_editable_by_user?
Query(Story)

# Q 3272 : # @story.is_editable_by_user?
Query(Story)

# Q 3273 : # @user.id
Query(User)

# Q 3274 : # @user.id
Query(User)

# Q 3275 : # stories.top(length)
Query(Story)

# Q 3276 : # stories.top
Query(Story)

# Q 3277 : # stories.top
Query(Story)

# Q 3278 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, @comments.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 3279 : # Vote.comment_votes_by_user_for_comment_ids_hash(@user.id, @comments.map { |c|
#   
#   c.id
# })
Query(Vote)

# Q 3280 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 3281 : # @user.id
Query(User)

# Q 3282 : # @comments.map
Query(Comment)

# Q 3283 : # Vote.comment_votes_by_user_for_comment_ids_hash
Query(Vote)

# Q 3284 : # @user.id
Query(User)

# Q 3285 : # @comments.map
Query(Comment)

# Q 3286 : # @comments.each
Query(Comment)

# Q 3287 : # @comments.each
Query(Comment)

# Q 3288 : # self.is_new?
Query(User)

# Q 3289 : # self.karma
Query(User)
.select('karma')
# Q 3290 : # self.is_new?
Query(User)

# Q 3291 : # self.karma
Query(User)
.select('karma')
# Q 3292 : # @story.url_is_editable_by_user?(@user)
Query(Story)

# Q 3293 : # @story.url_is_editable_by_user?
Query(Story)

# Q 3294 : # @story.url_is_editable_by_user?
Query(Story)

# Q 3295 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3296 : # self.user
Query(User)
.where("id = ?")
# Q 3297 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3298 : # self.story
Query(Story)
.where("id = ?")
# Q 3299 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3300 : # self.user
Query(User)
.where("id = ?")
# Q 3301 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3302 : # self.story
Query(Story)
.where("id = ?")
# Q 3303 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3304 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3305 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3306 : # self.user
Query(User)
.where("id = ?")
# Q 3307 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3308 : # self.story
Query(Story)
.where("id = ?")
# Q 3309 : # self.plaintext_comment
Query(Comment)

# Q 3310 : # self.plaintext_comment
Query(Comment)

# Q 3311 : # self.plaintext_comment
Query(Comment)

# Q 3312 : # @user.save!
Query(User)

# Q 3313 : # @user.save!
Query(User)

# Q 3314 : # self.url
Query(Comment)

# Q 3315 : # self.url
Query(Comment)

# Q 3316 : # self.url
Query(Comment)

# Q 3317 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3318 : # self.user
Query(User)
.where("id = ?")
# Q 3319 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3320 : # self.user
Query(User)
.where("id = ?")
# Q 3321 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3322 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3323 : # self.user
Query(User)
.where("id = ?")
# Q 3324 : # self.can_submit_stories?
Query(User)

# Q 3325 : # self.can_submit_stories?
Query(User)

# Q 3326 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject(&:+).to_f
Query(Story)
.where("story_id = ?")
# Q 3327 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject(&:+)
Query(Story)
.where("story_id = ?")
# Q 3328 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject
Query(Story)
.where("story_id = ?")
# Q 3329 : # self.merged_stories.map
Query(Story)
.where("story_id = ?")
# Q 3330 : # self.merged_stories
Query(Story)
.where("story_id = ?")
# Q 3331 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject(&:+).to_f
Query(Story)
.where("story_id = ?")
# Q 3332 : # self.merged_stories.map { |s|
#   
#   s.score
# }.inject
Query(Story)
.where("story_id = ?")
# Q 3333 : # self.merged_stories.map
Query(Story)
.where("story_id = ?")
# Q 3334 : # self.merged_stories
Query(Story)
.where("story_id = ?")
# Q 3335 : # @story.save
Query(Story)

# Q 3336 : # @story.save
Query(Story)

# Q 3337 : # @story.comments_path
Query(Story)

# Q 3338 : # @story.comments_path
Query(Story)

# Q 3339 : # @user.username
Query(User)
.select('username')
# Q 3340 : # @user.username
Query(User)
.select('username')
# Q 3341 : # @user.username
Query(User)
.select('username')
# Q 3342 : # @user.username
Query(User)
.select('username')
# Q 3343 : # @user.username
Query(User)
.select('username')
# Q 3344 : # self.is_new?
Query(User)

# Q 3345 : # self.karma
Query(User)
.select('karma')
# Q 3346 : # self.is_new?
Query(User)

# Q 3347 : # self.karma
Query(User)
.select('karma')
# Q 3348 : # self.upvotes
Query(Story)
.select('upvotes')
# Q 3349 : # self.upvotes
Query(Story)
.select('upvotes')
# Q 3350 : # @user.upvoted_stories.order("votes.id DESC")
Query(User)
.where("user_id = ?")
.order('id')
.order('id')
# Q 3351 : # @user.upvoted_stories.order
Query(User)
.where("user_id = ?")
# Q 3352 : # @user.upvoted_stories
Query(User)
.where("user_id = ?")
# Q 3353 : # @user.upvoted_stories.order
Query(User)
.where("user_id = ?")
# Q 3354 : # @user.upvoted_stories
Query(User)
.where("user_id = ?")
# Q 3355 : # self.upvotes
Query(Story)
.select('upvotes')
# Q 3356 : # self.upvotes
Query(Story)
.select('upvotes')
# Q 3357 : # self.upvotes
Query(Story)
.select('upvotes')
# Q 3358 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 3359 : # self.parent_comment_id
Query(Comment)
.select('parent_comment_id')
# Q 3360 : # self.is_moderator?
Query(User)

# Q 3361 : # self.is_moderator?
Query(User)

# Q 3362 : # self.parent_comment.try(:user)
Query(Comment)
.where("id = ?")
.select('user')
# Q 3363 : # self.parent_comment.try(:user)
Query(Comment)
.where("id = ?")
.select('user')
# Q 3364 : # self.parent_comment.try
Query(Comment)
.where("id = ?")
# Q 3365 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 3366 : # self.parent_comment.try
Query(Comment)
.where("id = ?")
# Q 3367 : # self.parent_comment
Query(Comment)
.where("id = ?")
# Q 3368 : # self.karma
Query(User)
.select('karma')
# Q 3369 : # self.karma
Query(User)
.select('karma')
# Q 3370 : # self.user.id
Query(User)
.where("id = ?")
# Q 3371 : # self.user
Query(User)
.where("id = ?")
# Q 3372 : # self.user.id
Query(User)
.where("id = ?")
# Q 3373 : # self.user
Query(User)
.where("id = ?")
# Q 3374 : # Vote.vote_thusly_on_story_or_comment_for_user_because(0, story.id, nil, @user.id, nil)
Query(Vote)

# Q 3375 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3376 : # story.id
Query(Story)

# Q 3377 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3378 : # story.id
Query(Story)

# Q 3379 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 3380 : # @user.rss_token
Query(User)
.select('rss_token')
# Q 3381 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3382 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3383 : # User.where(:username => params[:user])
Query(User)
.where("username = ?")
# Q 3384 : # User.where(:username => params[:user]).first!
Query(User)
.where("username = ?")
.return_limit('1')
# Q 3385 : # self.karma
Query(User)
.select('karma')
# Q 3386 : # self.karma
Query(User)
.select('karma')
# Q 3387 : # @user.id
Query(User)

# Q 3388 : # @user.id
Query(User)

# Q 3389 : # self.session_token.blank?
Query(User)
.select('session_token')
# Q 3390 : # self.session_token
Query(User)
.select('session_token')
# Q 3391 : # self.session_token.blank?
Query(User)
.select('session_token')
# Q 3392 : # self.session_token
Query(User)
.select('session_token')
# Q 3393 : # self.created_at
Query(Story)
.select('created_at')
# Q 3394 : # self.created_at
Query(Story)
.select('created_at')
# Q 3395 : # @user.username
Query(User)
.select('username')
# Q 3396 : # @user.username
Query(User)
.select('username')
# Q 3397 : # @user.username
Query(User)
.select('username')
# Q 3398 : # @user.username
Query(User)
.select('username')
# Q 3399 : # @user.username
Query(User)
.select('username')
# Q 3400 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3401 : # self.user
Query(User)
.where("id = ?")
# Q 3402 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3403 : # self.story
Query(Story)
.where("id = ?")
# Q 3404 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3405 : # self.user
Query(User)
.where("id = ?")
# Q 3406 : # self.story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 3407 : # self.story
Query(Story)
.where("id = ?")
# Q 3408 : # self.plaintext_comment
Query(Comment)

# Q 3409 : # self.plaintext_comment
Query(Comment)

# Q 3410 : # self.mailing_list_token.blank?
Query(User)
.select('mailing_list_token')
# Q 3411 : # self.mailing_list_token
Query(User)
.select('mailing_list_token')
# Q 3412 : # self.mailing_list_token.blank?
Query(User)
.select('mailing_list_token')
# Q 3413 : # self.mailing_list_token
Query(User)
.select('mailing_list_token')
# Q 3414 : # user.is_moderator?
Query(User)

# Q 3415 : # user.id
Query(User)

# Q 3416 : # self.user_id
Query(Story)
.select('user_id')
# Q 3417 : # user.is_moderator?
Query(User)

# Q 3418 : # user.id
Query(User)

# Q 3419 : # self.user_id
Query(Story)
.select('user_id')
# Q 3420 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, story.id, nil, @user.id, nil)
Query(Vote)

# Q 3421 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3422 : # story.id
Query(Story)

# Q 3423 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3424 : # story.id
Query(Story)

# Q 3425 : # self.url
Query(Comment)

# Q 3426 : # self.url
Query(Comment)

# Q 3427 : # @user.id
Query(User)

# Q 3428 : # @user.id
Query(User)

# Q 3429 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3430 : # self.user
Query(User)
.where("id = ?")
# Q 3431 : # self.user.username
Query(User)
.where("id = ?")
.select('username')
# Q 3432 : # self.user
Query(User)
.where("id = ?")
# Q 3433 : # @user.id
Query(User)

# Q 3434 : # @user.id
Query(User)

# Q 3435 : # Comment.where(:thread_id => thread_ids).includes(:user, :story, :hat, :votes => :user).arrange_for_user(@user)
Query(Vote)
.where("thread_id = ?")
.includes('user')
.includes('story')
.includes('hat')
.includes('votes')
.includes('user')
# Q 3436 : # Comment.where(:thread_id => thread_ids).includes(:user, :story, :hat, :votes => :user).arrange_for_user(@user)
Query(Vote)
.where("thread_id = ?")
.includes('user')
.includes('story')
.includes('hat')
.includes('votes')
.includes('user')
# Q 3437 : # Comment.where(:thread_id => thread_ids).includes(:user, :story, :hat, :votes => :user).arrange_for_user
Query(Vote)
.where("thread_id = ?")
.includes('user')
.includes('story')
.includes('hat')
.includes('votes')
.includes('user')
# Q 3438 : # Comment.where(:thread_id => thread_ids).includes(:user, :story, :hat, :votes => :user)
Query(Vote)
.where("thread_id = ?")
.includes('user')
.includes('story')
.includes('hat')
.includes('votes')
.includes('user')
# Q 3439 : # Comment.where(:thread_id => thread_ids).includes
Query(Comment)
.where("thread_id = ?")
# Q 3440 : # Comment.where(:thread_id => thread_ids)
Query(Comment)
.where("thread_id = ?")
# Q 3441 : # Comment.where(:thread_id => thread_ids).includes(:user, :story, :hat, :votes => :user).arrange_for_user
Query(Vote)
.where("thread_id = ?")
.includes('user')
.includes('story')
.includes('hat')
.includes('votes')
.includes('user')
# Q 3442 : # Comment.where(:thread_id => thread_ids).includes
Query(Comment)
.where("thread_id = ?")
# Q 3443 : # self.rss_token.blank?
Query(User)
.select('rss_token')
# Q 3444 : # self.rss_token
Query(User)
.select('rss_token')
# Q 3445 : # self.rss_token.blank?
Query(User)
.select('rss_token')
# Q 3446 : # self.rss_token
Query(User)
.select('rss_token')
# Q 3447 : # user.id
Query(User)

# Q 3448 : # self.user_id
Query(Story)
.select('user_id')
# Q 3449 : # user.can_offer_suggestions?
Query(User)

# Q 3450 : # user.id
Query(User)

# Q 3451 : # self.user_id
Query(Story)
.select('user_id')
# Q 3452 : # user.can_offer_suggestions?
Query(User)

# Q 3453 : # self.comment
Query(Comment)
.select('comment')
# Q 3454 : # self.comment
Query(Comment)
.select('comment')
# Q 3455 : # @user.tag_filters.map
Query(TagFilter)
.where("user_id = ?")
# Q 3456 : # @user.tag_filters
Query(TagFilter)
.where("user_id = ?")
# Q 3457 : # @user.tag_filters.map
Query(TagFilter)
.where("user_id = ?")
# Q 3458 : # @user.tag_filters
Query(TagFilter)
.where("user_id = ?")
# Q 3459 : # Keystore.value_for
Query(Keystore)

# Q 3460 : # self.id
Query(User)

# Q 3461 : # Keystore.value_for
Query(Keystore)

# Q 3462 : # self.id
Query(User)

# Q 3463 : # self.taggings.select { |t|
#   
#   t.tag && t.tag.privileged?
# }.any?
Query(Tagging)
.where("story_id = ?")
# Q 3464 : # self.taggings.select
Query(Tagging)
.where("story_id = ?")
# Q 3465 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3466 : # self.taggings.select { |t|
#   
#   t.tag && t.tag.privileged?
# }.any?
Query(Tagging)
.where("story_id = ?")
# Q 3467 : # self.taggings.select
Query(Tagging)
.where("story_id = ?")
# Q 3468 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3469 : # comments.group_by(&:thread_id)
Query(Comment)

# Q 3470 : # comments.group_by(&:thread_id)
Query(Comment)

# Q 3471 : # comments.group_by
Query(Comment)

# Q 3472 : # comments.group_by
Query(Comment)

# Q 3473 : # @user.can_downvote?(story)
Query(User)

# Q 3474 : # @user.can_downvote?
Query(User)

# Q 3475 : # @user.can_downvote?
Query(User)

# Q 3476 : # Comment.connection.execute
Query(Comment)

# Q 3477 : # Comment.connection
Query(Comment)

# Q 3478 : # Comment.table_name
Query(Comment)

# Q 3479 : # Comment.connection.execute
Query(Comment)

# Q 3480 : # Comment.connection
Query(Comment)

# Q 3481 : # Comment.table_name
Query(Comment)

# Q 3482 : # StoryRepository.new(@user, exclude_tags: filtered_tag_ids)
Query(StoryRepository)

# Q 3483 : # StoryRepository.new
Query(StoryRepository)

# Q 3484 : # StoryRepository.new
Query(StoryRepository)

# Q 3485 : # Vote.comment_votes_by_user_for_story_hash(@user.id, comments.map(&:story_id).uniq)
Query(Vote)

# Q 3486 : # Vote.comment_votes_by_user_for_story_hash(@user.id, comments.map(&:story_id).uniq)
Query(Vote)

# Q 3487 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3488 : # @user.id
Query(User)

# Q 3489 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3490 : # @user.id
Query(User)

# Q 3491 : # self.email.strip.downcase
Query(User)
.select('email')
# Q 3492 : # self.email.strip
Query(User)
.select('email')
# Q 3493 : # self.email
Query(User)
.select('email')
# Q 3494 : # self.email.strip.downcase
Query(User)
.select('email')
# Q 3495 : # self.email.strip
Query(User)
.select('email')
# Q 3496 : # self.email
Query(User)
.select('email')
# Q 3497 : # comments.map(&:story_id).uniq
Query(Comment)
.distinct('')
# Q 3498 : # comments.map(&:story_id)
Query(Comment)

# Q 3499 : # comments.map
Query(Comment)

# Q 3500 : # comments.map(&:story_id).uniq
Query(Comment)
.distinct('')
# Q 3501 : # comments.map
Query(Comment)

# Q 3502 : # self.calculated_confidence
Query(Comment)

# Q 3503 : # self.calculated_confidence
Query(Comment)

# Q 3504 : # Vote.vote_thusly_on_story_or_comment_for_user_because(-1, story.id, nil, @user.id, params[:reason])
Query(Vote)

# Q 3505 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3506 : # story.id
Query(Story)

# Q 3507 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3508 : # story.id
Query(Story)

# Q 3509 : # comments.each
Query(Comment)

# Q 3510 : # comments.each
Query(Comment)

# Q 3511 : # self.id.to_i
Query(Comment)

# Q 3512 : # self.id
Query(Comment)

# Q 3513 : # self.id.to_i
Query(Comment)

# Q 3514 : # self.id
Query(Comment)

# Q 3515 : # @user.id
Query(User)

# Q 3516 : # @user.id
Query(User)

# Q 3517 : # self.story.recalculate_hotness!
Query(Story)
.where("id = ?")
# Q 3518 : # self.story
Query(Story)
.where("id = ?")
# Q 3519 : # self.story.recalculate_hotness!
Query(Story)
.where("id = ?")
# Q 3520 : # self.story
Query(Story)
.where("id = ?")
# Q 3521 : # self.editor
Query(Story)

# Q 3522 : # self.user
Query(User)
.where("id = ?")
# Q 3523 : # self.editor
Query(Story)

# Q 3524 : # self.user
Query(User)
.where("id = ?")
# Q 3525 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 3526 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3527 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 3528 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3529 : # self.is_moderated?
Query(Comment)

# Q 3530 : # self.is_moderated?
Query(Comment)

# Q 3531 : # self.moderation.try(:moderator).try(:username).to_s
Query(Moderation)
.where("id = ?")
.select('moderator')
.select('username')
# Q 3532 : # self.moderation.try(:moderator).try(:username)
Query(Moderation)
.where("id = ?")
.select('moderator')
.select('username')
# Q 3533 : # self.moderation.try(:moderator).try
Query(Moderation)
.where("id = ?")
.select('moderator')
# Q 3534 : # self.moderation.try(:moderator)
Query(Moderation)
.where("id = ?")
.select('moderator')
# Q 3535 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3536 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3537 : # self.moderation.try(:moderator).try(:username).to_s
Query(Moderation)
.where("id = ?")
.select('moderator')
.select('username')
# Q 3538 : # self.moderation.try(:moderator).try
Query(Moderation)
.where("id = ?")
.select('moderator')
# Q 3539 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3540 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3541 : # self.moderation.try(:reason)
Query(Moderation)
.where("id = ?")
.select('reason')
# Q 3542 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3543 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3544 : # self.moderation.try
Query(Moderation)
.where("id = ?")
# Q 3545 : # self.moderation
Query(Moderation)
.where("id = ?")
# Q 3546 : # self.user.is_banned?
Query(User)
.where("id = ?")
# Q 3547 : # self.user
Query(User)
.where("id = ?")
# Q 3548 : # self.user.is_banned?
Query(User)
.where("id = ?")
# Q 3549 : # self.user
Query(User)
.where("id = ?")
# Q 3550 : # HiddenStory.hide_story_for_user(story.id, @user.id)
Query(HiddenStory)

# Q 3551 : # HiddenStory.hide_story_for_user
Query(HiddenStory)

# Q 3552 : # story.id
Query(Story)

# Q 3553 : # @user.id
Query(User)

# Q 3554 : # HiddenStory.hide_story_for_user
Query(HiddenStory)

# Q 3555 : # story.id
Query(Story)

# Q 3556 : # @user.id
Query(User)

# Q 3557 : # StoriesPaginator.new(scope, page, @user).get
Query(StoriesPaginator)

# Q 3558 : # StoriesPaginator.new(scope, page, @user)
Query(StoriesPaginator)

# Q 3559 : # StoriesPaginator.new
Query(StoriesPaginator)

# Q 3560 : # StoriesPaginator.new(scope, page, @user).get
Query(StoriesPaginator)

# Q 3561 : # StoriesPaginator.new
Query(StoriesPaginator)

# Q 3562 : # @user.can_invite?
Query(User)

# Q 3563 : # ReadRibbon.hide_replies_for(story.id, @user.id)
Query(ReadRibbon)

# Q 3564 : # ReadRibbon.hide_replies_for
Query(ReadRibbon)

# Q 3565 : # story.id
Query(Story)

# Q 3566 : # @user.id
Query(User)

# Q 3567 : # ReadRibbon.hide_replies_for
Query(ReadRibbon)

# Q 3568 : # story.id
Query(Story)

# Q 3569 : # @user.id
Query(User)

# Q 3570 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction? || t.tag.is_media?
# }.any?
Query(Tagging)
.where("story_id = ?")
# Q 3571 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3572 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3573 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction? || t.tag.is_media?
# }.any?
Query(Tagging)
.where("story_id = ?")
# Q 3574 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 3575 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 3576 : # @user.disabled_invite_reason
Query(User)
.select('disabled_invite_reason')
# Q 3577 : # Keystore.put
Query(Keystore)

# Q 3578 : # self.id
Query(User)

# Q 3579 : # self.comments.active.count
Query(Comment)
.where("user_id = ?")
# Q 3580 : # self.comments.active
Query(Comment)
.where("user_id = ?")
# Q 3581 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3582 : # Keystore.put
Query(Keystore)

# Q 3583 : # self.id
Query(User)

# Q 3584 : # self.comments.active.count
Query(Comment)
.where("user_id = ?")
# Q 3585 : # self.comments.active
Query(Comment)
.where("user_id = ?")
# Q 3586 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3587 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3588 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3589 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3590 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3591 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3592 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3593 : # User.transaction
Query(User)

# Q 3594 : # User.transaction
Query(User)

# Q 3595 : # self.comments.where("upvotes - downvotes < 0").each
Query(Comment)
.where("user_id = ?")
.where(" = ?")
# Q 3596 : # self.comments.where("upvotes - downvotes < 0")
Query(Comment)
.where("user_id = ?")
.where(" = ?")
# Q 3597 : # self.comments.where
Query(Comment)
.where("user_id = ?")
# Q 3598 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3599 : # self.comments.where("upvotes - downvotes < 0").each { |c|
#   
#   c.delete_for_user(self)
# }
Query(Comment)
.where("user_id = ?")
.where(" = ?")
# Q 3600 : # self.comments.where("upvotes - downvotes < 0").each
Query(Comment)
.where("user_id = ?")
.where(" = ?")
# Q 3601 : # self.comments.where
Query(Comment)
.where("user_id = ?")
# Q 3602 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3603 : # HiddenStory.where(:user_id => @user.id, :story_id => story.id).delete_all
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3604 : # HiddenStory.where(:user_id => @user.id, :story_id => story.id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3605 : # @user.id
Query(User)

# Q 3606 : # story.id
Query(Story)

# Q 3607 : # HiddenStory.where(:user_id => @user.id, :story_id => story.id).delete_all
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3608 : # @user.id
Query(User)

# Q 3609 : # story.id
Query(Story)

# Q 3610 : # self.title_as_url
Query(Story)

# Q 3611 : # self.title_as_url
Query(Story)

# Q 3612 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3613 : # self.user
Query(User)
.where("id = ?")
# Q 3614 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3615 : # self.user
Query(User)
.where("id = ?")
# Q 3616 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 3617 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 3618 : # self.sent_messages.each do |m|
#   
#   m.deleted_by_author = true
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 3619 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 3620 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 3621 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3622 : # self.user
Query(User)
.where("id = ?")
# Q 3623 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3624 : # self.user
Query(User)
.where("id = ?")
# Q 3625 : # self.title_as_url
Query(Story)

# Q 3626 : # self.title_as_url
Query(Story)

# Q 3627 : # self.story
Query(Story)
.where("id = ?")
# Q 3628 : # self.story.user_is_author?
Query(Story)
.where("id = ?")
# Q 3629 : # self.story
Query(Story)
.where("id = ?")
# Q 3630 : # self.story
Query(Story)
.where("id = ?")
# Q 3631 : # self.story.user_is_author?
Query(Story)
.where("id = ?")
# Q 3632 : # self.story
Query(Story)
.where("id = ?")
# Q 3633 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 3634 : # self.story
Query(Story)
.where("id = ?")
# Q 3635 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3636 : # self.story.user_id
Query(Story)
.where("id = ?")
.select('user_id')
# Q 3637 : # self.story
Query(Story)
.where("id = ?")
# Q 3638 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3639 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 3640 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 3641 : # self.received_messages.each do |m|
#   
#   m.deleted_by_recipient = true
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 3642 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 3643 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 3644 : # self.generated_markeddown_description
Query(Story)

# Q 3645 : # self.generated_markeddown_description
Query(Story)

# Q 3646 : # self.generated_markeddown_description
Query(Story)

# Q 3647 : # SavedStory.save_story_for_user(story.id, @user.id)
Query(SavedStory)

# Q 3648 : # SavedStory.save_story_for_user
Query(SavedStory)

# Q 3649 : # story.id
Query(Story)

# Q 3650 : # @user.id
Query(User)

# Q 3651 : # SavedStory.save_story_for_user
Query(SavedStory)

# Q 3652 : # story.id
Query(Story)

# Q 3653 : # @user.id
Query(User)

# Q 3654 : # self.invitations.destroy_all
Query(Invitation)
.where("user_id = ?")
# Q 3655 : # self.invitations
Query(Invitation)
.where("user_id = ?")
# Q 3656 : # self.invitations.destroy_all
Query(Invitation)
.where("user_id = ?")
# Q 3657 : # self.invitations.destroy_all
Query(Invitation)
.where("user_id = ?")
# Q 3658 : # self.invitations
Query(Invitation)
.where("user_id = ?")
# Q 3659 : # self.description.present?
Query(Story)
.select('description')
# Q 3660 : # self.description
Query(Story)
.select('description')
# Q 3661 : # self.description.present?
Query(Story)
.select('description')
# Q 3662 : # self.description
Query(Story)
.select('description')
# Q 3663 : # Comment.where(:short_id => params[:id]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 3664 : # Comment.where(:short_id => params[:id]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 3665 : # Comment.where(:short_id => params[:id])
Query(Comment)
.where("short_id = ?")
# Q 3666 : # Comment.where(:short_id => params[:id]).first
Query(Comment)
.where("short_id = ?")
.return_limit('1')
# Q 3667 : # user.is_moderator?
Query(User)

# Q 3668 : # user.is_moderator?
Query(User)

# Q 3669 : # self.check_session_token
Query(User)

# Q 3670 : # self.check_session_token
Query(User)

# Q 3671 : # self.check_session_token
Query(User)

# Q 3672 : # self.markeddown_description.gsub(/<[^>]*>/, "")
Query(Story)
.select('markeddown_description')
# Q 3673 : # self.markeddown_description.gsub
Query(Story)
.select('markeddown_description')
# Q 3674 : # self.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 3675 : # self.markeddown_description.gsub
Query(Story)
.select('markeddown_description')
# Q 3676 : # self.markeddown_description
Query(Story)
.select('markeddown_description')
# Q 3677 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3678 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3679 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 3680 : # @user.id
Query(User)

# Q 3681 : # Vote.where(:user_id => @user.id, :story_id => comment.story_id, :comment_id => comment.id).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3682 : # @user.id
Query(User)

# Q 3683 : # user.id
Query(User)

# Q 3684 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3685 : # user.id
Query(User)

# Q 3686 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3687 : # self.story_cache
Query(Story)
.select('story_cache')
# Q 3688 : # self.story_cache
Query(Story)
.select('story_cache')
# Q 3689 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 3690 : # comment.id
Query(Comment)

# Q 3691 : # comment.story_id
Query(Comment)
.select('story_id')
# Q 3692 : # comment.id
Query(Comment)

# Q 3693 : # self.save!
Query(User)

# Q 3694 : # self.save!
Query(User)

# Q 3695 : # self.save!
Query(User)

# Q 3696 : # SavedStory.where(:user_id => @user.id, :story_id => story.id).delete_all
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3697 : # SavedStory.where(:user_id => @user.id, :story_id => story.id)
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3698 : # @user.id
Query(User)

# Q 3699 : # story.id
Query(Story)

# Q 3700 : # SavedStory.where(:user_id => @user.id, :story_id => story.id).delete_all
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 3701 : # @user.id
Query(User)

# Q 3702 : # story.id
Query(Story)

# Q 3703 : # User.transaction
Query(User)

# Q 3704 : # User.transaction
Query(User)

# Q 3705 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 3706 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 3707 : # self.sent_messages.each do |m|
#   
#   m.deleted_by_author = false
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 3708 : # self.sent_messages.each
Query(Message)
.where("user_id = ?")
# Q 3709 : # self.sent_messages
Query(Message)
.where("user_id = ?")
# Q 3710 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3711 : # self.score
Query(Comment)

# Q 3712 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3713 : # self.score
Query(Comment)

# Q 3714 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3715 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3716 : # Story.new(story_params)
Query(Story)

# Q 3717 : # Story.new(story_params)
Query(Story)

# Q 3718 : # Story.new
Query(Story)

# Q 3719 : # Story.new
Query(Story)

# Q 3720 : # @story.check_already_posted
Query(Story)

# Q 3721 : # @story.check_already_posted
Query(Story)

# Q 3722 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 3723 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 3724 : # self.received_messages.each do |m|
#   
#   m.deleted_by_recipient = false
#   m.save
# end
Query(Message)
.where("user_id = ?")
# Q 3725 : # self.received_messages.each
Query(Message)
.where("user_id = ?")
# Q 3726 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 3727 : # self.url.blank?
Query(Story)
.select('url')
# Q 3728 : # self.url
Query(Story)
.select('url')
# Q 3729 : # self.url.blank?
Query(Story)
.select('url')
# Q 3730 : # self.url
Query(Story)
.select('url')
# Q 3731 : # user.id
Query(User)

# Q 3732 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3733 : # user.id
Query(User)

# Q 3734 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3735 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "").gsub(/^www\d*\.(.+\..+)/, "\1")
Query(Story)
.select('url')
# Q 3736 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "").gsub
Query(Story)
.select('url')
# Q 3737 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "")
Query(Story)
.select('url')
# Q 3738 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub
Query(Story)
.select('url')
# Q 3739 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "")
Query(Story)
.select('url')
# Q 3740 : # self.url.gsub(/^[^:]+:\/\//, "").gsub
Query(Story)
.select('url')
# Q 3741 : # self.url.gsub(/^[^:]+:\/\//, "")
Query(Story)
.select('url')
# Q 3742 : # self.url.gsub
Query(Story)
.select('url')
# Q 3743 : # self.url
Query(Story)
.select('url')
# Q 3744 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub(/:\d+$/, "").gsub
Query(Story)
.select('url')
# Q 3745 : # self.url.gsub(/^[^:]+:\/\//, "").gsub(/\/.*/, "").gsub
Query(Story)
.select('url')
# Q 3746 : # self.url.gsub(/^[^:]+:\/\//, "").gsub
Query(Story)
.select('url')
# Q 3747 : # self.url.gsub
Query(Story)
.select('url')
# Q 3748 : # self.url
Query(Story)
.select('url')
# Q 3749 : # self.is_moderated?
Query(Comment)

# Q 3750 : # self.is_moderated?
Query(Comment)

# Q 3751 : # self.save!
Query(User)

# Q 3752 : # self.save!
Query(User)

# Q 3753 : # self.save!
Query(User)

# Q 3754 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3755 : # self.updated_at.to_i
Query(Comment)
.select('updated_at')
# Q 3756 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3757 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3758 : # self.updated_at.to_i
Query(Comment)
.select('updated_at')
# Q 3759 : # self.updated_at
Query(Comment)
.select('updated_at')
# Q 3760 : # self.created_at.to_i
Query(Comment)
.select('created_at')
# Q 3761 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3762 : # self.created_at.to_i
Query(Comment)
.select('created_at')
# Q 3763 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3764 : # User.find_by!(:username => "inactive-user")
Query(User)
.where("username = ?")
# Q 3765 : # User.find_by!(:username => "inactive-user")
Query(User)
.where("username = ?")
# Q 3766 : # self.comments.update_all(:user_id => inactive_user.id)
Query(Comment)
.where("user_id = ?")
# Q 3767 : # self.comments.update_all
Query(Comment)
.where("user_id = ?")
# Q 3768 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3769 : # self.comments.update_all
Query(Comment)
.where("user_id = ?")
# Q 3770 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 3771 : # @user.is_moderator?
Query(User)

# Q 3772 : # @user.is_moderator?
Query(User)

# Q 3773 : # self.domain
Query(Story)

# Q 3774 : # self.domain
Query(Story)

# Q 3775 : # self.save!
Query(User)

# Q 3776 : # self.save!
Query(User)

# Q 3777 : # self.url.present?
Query(Story)
.select('url')
# Q 3778 : # self.url
Query(Story)
.select('url')
# Q 3779 : # self.url.present?
Query(Story)
.select('url')
# Q 3780 : # self.url
Query(Story)
.select('url')
# Q 3781 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3782 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3783 : # Story.where(:short_id => params[:story_id])
Query(Story)
.where("short_id = ?")
# Q 3784 : # Story.where(:short_id => params[:story_id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3785 : # user.is_moderator?
Query(User)

# Q 3786 : # user.is_moderator?
Query(User)

# Q 3787 : # User.transaction
Query(User)

# Q 3788 : # User.transaction
Query(User)

# Q 3789 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try(:vote)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
.select('vote')
# Q 3790 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try(:vote)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
.select('vote')
# Q 3791 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3792 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3793 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 3794 : # @user.id
Query(User)

# Q 3795 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first.try
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3796 : # Vote.where(:user_id => @user.id, :story_id => story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3797 : # @user.id
Query(User)

# Q 3798 : # user.id
Query(User)

# Q 3799 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3800 : # self.is_moderated?
Query(Comment)

# Q 3801 : # user.id
Query(User)

# Q 3802 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3803 : # self.is_moderated?
Query(Comment)

# Q 3804 : # self.save!
Query(User)

# Q 3805 : # self.save!
Query(User)

# Q 3806 : # self.save!
Query(User)

# Q 3807 : # story.id
Query(Story)

# Q 3808 : # story.id
Query(Story)

# Q 3809 : # Moderation.new
Query(Moderation)

# Q 3810 : # Moderation.new
Query(Moderation)

# Q 3811 : # m = Moderation.new
Query(Moderation)

# Q 3812 : # Moderation.new
Query(Moderation)

# Q 3813 : # user.id
Query(User)

# Q 3814 : # user.id
Query(User)

# Q 3815 : # user.id
Query(User)

# Q 3816 : # self.title.to_s.split("").map { |chr|
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
# Q 3817 : # self.title.to_s.split("").map { |chr|
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
# Q 3818 : # self.title.to_s.split("").map { |chr|
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
# Q 3819 : # self.title.to_s.split("").map
Query(Story)
.select('title')
# Q 3820 : # self.title.to_s.split("")
Query(Story)
.select('title')
# Q 3821 : # self.title.to_s.split
Query(Story)
.select('title')
# Q 3822 : # self.title.to_s
Query(Story)
.select('title')
# Q 3823 : # self.title
Query(Story)
.select('title')
# Q 3824 : # self.title.to_s.split("").map { |chr|
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
# Q 3825 : # self.title.to_s.split("").map
Query(Story)
.select('title')
# Q 3826 : # self.title.to_s.split
Query(Story)
.select('title')
# Q 3827 : # self.title.to_s
Query(Story)
.select('title')
# Q 3828 : # self.title
Query(Story)
.select('title')
# Q 3829 : # self.id
Query(User)

# Q 3830 : # self.id
Query(User)

# Q 3831 : # self.id
Query(User)

# Q 3832 : # self.hat
Query(Hat)
.where("id = ?")
# Q 3833 : # self.hat.modlog_use
Query(Hat)
.where("id = ?")
.select('modlog_use')
# Q 3834 : # self.hat
Query(Hat)
.where("id = ?")
# Q 3835 : # self.hat
Query(Hat)
.where("id = ?")
# Q 3836 : # self.hat.modlog_use
Query(Hat)
.where("id = ?")
.select('modlog_use')
# Q 3837 : # self.hat
Query(Hat)
.where("id = ?")
# Q 3838 : # Hat.new
Query(Hat)

# Q 3839 : # Hat.new
Query(Hat)

# Q 3840 : # h = Hat.new
Query(Hat)

# Q 3841 : # Hat.new
Query(Hat)

# Q 3842 : # self.id
Query(User)

# Q 3843 : # self.id
Query(User)

# Q 3844 : # self.id
Query(User)

# Q 3845 : # Moderation.new
Query(Moderation)

# Q 3846 : # Moderation.new
Query(Moderation)

# Q 3847 : # Moderation.new
Query(Moderation)

# Q 3848 : # user.id
Query(User)

# Q 3849 : # user.id
Query(User)

# Q 3850 : # user.id
Query(User)

# Q 3851 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3852 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3853 : # self.created_at
Query(Comment)
.select('created_at')
# Q 3854 : # self.id
Query(Comment)

# Q 3855 : # self.id
Query(Comment)

# Q 3856 : # self.id
Query(Comment)

# Q 3857 : # user.id
Query(User)

# Q 3858 : # user.id
Query(User)

# Q 3859 : # user.id
Query(User)

# Q 3860 : # self.hat.hat
Query(Hat)
.where("id = ?")
.select('hat')
# Q 3861 : # self.hat
Query(Hat)
.where("id = ?")
# Q 3862 : # self.hat.hat
Query(Hat)
.where("id = ?")
.select('hat')
# Q 3863 : # self.hat
Query(Hat)
.where("id = ?")
# Q 3864 : # @user.is_moderator?
Query(User)

# Q 3865 : # @user.is_moderator?
Query(User)

# Q 3866 : # self.description
Query(Story)
.select('description')
# Q 3867 : # self.description
Query(Story)
.select('description')
# Q 3868 : # Story.where(:short_id => params[:story_id] || params[:id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3869 : # Story.where(:short_id => params[:story_id] || params[:id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3870 : # Story.where(:short_id => params[:story_id] || params[:id])
Query(Story)
.where("short_id = ?")
# Q 3871 : # Story.where(:short_id => params[:story_id] || params[:id]).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 3872 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id])).first
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 3873 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id])).first
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 3874 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id]))
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
# Q 3875 : # @user.id
Query(User)

# Q 3876 : # Story.where(:user_id => @user.id, :short_id => (
# params[:story_id] || params[:id])).first
Query(Story)
.where("user_id = ?")
.where("short_id = ?")
.return_limit('1')
# Q 3877 : # @user.id
Query(User)

# Q 3878 : # Keystore.increment_value_for
Query(Keystore)

# Q 3879 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3880 : # Keystore.increment_value_for
Query(Keystore)

# Q 3881 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3882 : # self.save!
Query(User)

# Q 3883 : # self.save!
Query(User)

# Q 3884 : # Story.connection.execute
Query(Story)

# Q 3885 : # Story.connection
Query(Story)

# Q 3886 : # Story.table_name
Query(Story)

# Q 3887 : # Story.connection.execute
Query(Story)

# Q 3888 : # Story.connection
Query(Story)

# Q 3889 : # Story.table_name
Query(Story)

# Q 3890 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3891 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3892 : # self.calculated_hotness
Query(Story)

# Q 3893 : # self.id.to_i
Query(Story)

# Q 3894 : # self.id
Query(Story)

# Q 3895 : # self.calculated_hotness
Query(Story)

# Q 3896 : # self.id.to_i
Query(Story)

# Q 3897 : # self.id
Query(Story)

# Q 3898 : # self.is_from_email
Query(Comment)
.select('is_from_email')
# Q 3899 : # self.is_from_email
Query(Comment)
.select('is_from_email')
# Q 3900 : # self.totp_secret.present?
Query(User)

# Q 3901 : # self.totp_secret
Query(User)

# Q 3902 : # self.totp_secret.present?
Query(User)

# Q 3903 : # self.totp_secret
Query(User)

# Q 3904 : # self.suggested_taggings.any?
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3905 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3906 : # self.suggested_titles.any?
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3907 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3908 : # self.suggested_taggings.any?
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3909 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 3910 : # self.suggested_titles.any?
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3911 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 3912 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3913 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3914 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil)
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
# Q 3915 : # @user.id
Query(User)

# Q 3916 : # @story.id
Query(Story)

# Q 3917 : # Vote.where(:user_id => @user.id, :story_id => @story.id, :comment_id => nil).first
Query(Vote)
.where("user_id = ?")
.where("story_id = ?")
.where("comment_id = ?")
.return_limit('1')
# Q 3918 : # @user.id
Query(User)

# Q 3919 : # @story.id
Query(Story)

# Q 3920 : # self.story.comments_path
Query(Story)
.where("id = ?")
# Q 3921 : # self.story
Query(Story)
.where("id = ?")
# Q 3922 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3923 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3924 : # self.story.comments_path
Query(Story)
.where("id = ?")
# Q 3925 : # self.story
Query(Story)
.where("id = ?")
# Q 3926 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3927 : # self.short_id
Query(Comment)
.select('short_id')
# Q 3928 : # HiddenStory.where(:story_id => self.id).count
Query(HiddenStory)
.where("story_id = ?")
# Q 3929 : # HiddenStory.where(:story_id => self.id)
Query(HiddenStory)
.where("story_id = ?")
# Q 3930 : # self.id
Query(Story)

# Q 3931 : # HiddenStory.where(:story_id => self.id).count
Query(HiddenStory)
.where("story_id = ?")
# Q 3932 : # self.id
Query(Story)

# Q 3933 : # @story.is_hidden_by_user?(@user)
Query(Story)

# Q 3934 : # @story.is_hidden_by_user?(@user)
Query(Story)

# Q 3935 : # @story.is_hidden_by_user?
Query(Story)

# Q 3936 : # @story.is_hidden_by_user?
Query(Story)

# Q 3937 : # @story.is_saved_by_user?(@user)
Query(Story)

# Q 3938 : # @story.is_saved_by_user?(@user)
Query(Story)

# Q 3939 : # @story.is_saved_by_user?
Query(Story)

# Q 3940 : # @story.is_saved_by_user?
Query(Story)

# Q 3941 : # self.created_at
Query(User)
.select('created_at')
# Q 3942 : # self.created_at
Query(User)
.select('created_at')
# Q 3943 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3944 : # self.user
Query(User)
.where("id = ?")
# Q 3945 : # self.user.is_active?
Query(User)
.where("id = ?")
# Q 3946 : # self.user
Query(User)
.where("id = ?")
# Q 3947 : # Vote.comment_votes_by_user_for_story_hash(@user.id, @story.id)
Query(Vote)

# Q 3948 : # Vote.comment_votes_by_user_for_story_hash(@user.id, @story.id)
Query(Vote)

# Q 3949 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3950 : # @user.id
Query(User)

# Q 3951 : # @story.id
Query(Story)

# Q 3952 : # Vote.comment_votes_by_user_for_story_hash
Query(Vote)

# Q 3953 : # @user.id
Query(User)

# Q 3954 : # @story.id
Query(Story)

# Q 3955 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3956 : # self.user
Query(User)
.where("id = ?")
# Q 3957 : # self.user.is_new?
Query(User)
.where("id = ?")
# Q 3958 : # self.user
Query(User)
.where("id = ?")
# Q 3959 : # @comments.each
Query(Comment)

# Q 3960 : # @comments.each
Query(Comment)

# Q 3961 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, self.story_id, self.id, self.user_id, nil, false)
Query(Vote)

# Q 3962 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3963 : # self.story_id
Query(Comment)
.select('story_id')
# Q 3964 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 3965 : # self.story_id
Query(Comment)
.select('story_id')
# Q 3966 : # self.id
Query(Comment)

# Q 3967 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3968 : # self.id
Query(Comment)

# Q 3969 : # self.user_id
Query(Comment)
.select('user_id')
# Q 3970 : # self.stories_submitted_count
Query(User)

# Q 3971 : # self.stories_submitted_count
Query(User)

# Q 3972 : # self.stories_submitted_count
Query(User)

# Q 3973 : # self.user_is_author?
Query(Story)

# Q 3974 : # self.user_is_author?
Query(Story)

# Q 3975 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3976 : # self.story
Query(Story)
.where("id = ?")
# Q 3977 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 3978 : # self.story
Query(Story)
.where("id = ?")
# Q 3979 : # self.stories.where(:user_is_author => true).count
Query(Story)
.where("user_id = ?")
.where("user_is_author = ?")
# Q 3980 : # self.stories.where(:user_is_author => true).count
Query(Story)
.where("user_id = ?")
.where("user_is_author = ?")
# Q 3981 : # self.stories.where(:user_is_author => true)
Query(Story)
.where("user_id = ?")
.where("user_is_author = ?")
# Q 3982 : # self.stories.where
Query(Story)
.where("user_id = ?")
# Q 3983 : # self.stories
Query(Story)
.where("user_id = ?")
# Q 3984 : # self.stories.where(:user_is_author => true).count
Query(Story)
.where("user_id = ?")
.where("user_is_author = ?")
# Q 3985 : # self.stories.where
Query(Story)
.where("user_id = ?")
# Q 3986 : # self.stories
Query(Story)
.where("user_id = ?")
# Q 3987 : # self.upvotes
Query(Comment)
.select('upvotes')
# Q 3988 : # self.downvotes
Query(Comment)
.select('downvotes')
# Q 3989 : # self.upvotes
Query(Comment)
.select('upvotes')
# Q 3990 : # self.downvotes
Query(Comment)
.select('downvotes')
# Q 3991 : # @user.can_submit_stories?
Query(User)

# Q 3992 : # @user.can_submit_stories?
Query(User)

# Q 3993 : # self.created_at
Query(Story)
.select('created_at')
# Q 3994 : # self.score
Query(Story)

# Q 3995 : # self.created_at
Query(Story)
.select('created_at')
# Q 3996 : # self.score
Query(Story)

# Q 3997 : # self.created_at
Query(Story)
.select('created_at')
# Q 3998 : # self.created_at
Query(Story)
.select('created_at')
# Q 3999 : # self.showing_downvotes_for_user?(u)
Query(Comment)

# Q 4000 : # self.showing_downvotes_for_user?
Query(Comment)

# Q 4001 : # self.showing_downvotes_for_user?
Query(Comment)

# Q 4002 : # self.about
Query(User)
.select('about')
# Q 4003 : # self.about
Query(User)
.select('about')
# Q 4004 : # Story.where(short_id: params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 4005 : # Story.where(short_id: params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 4006 : # Story.where(short_id: params[:id])
Query(Story)
.where("short_id = ?")
# Q 4007 : # Story.where(short_id: params[:id]).first!
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 4008 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order("COUNT(*) desc").first
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
.order('id')
.return_limit('1')
# Q 4009 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order("COUNT(*) desc")
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
.order('id')
# Q 4010 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 4011 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id])
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 4012 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 4013 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id })
Query(Tag)
.joins('stories')
.where("user_id = ?")
# Q 4014 : # Tag.active.joins(:stories).where
Query(Tag)
.joins('stories')
# Q 4015 : # Tag.active.joins(:stories)
Query(Tag)
.joins('stories')
# Q 4016 : # Tag.active.joins
Query(Tag)

# Q 4017 : # Tag.active
Query(Tag)

# Q 4018 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order("COUNT(*) desc").first
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
.order('id')
.return_limit('1')
# Q 4019 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group(Tag.arel_table[:id]).order
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 4020 : # Tag.active.joins(:stories).where(:stories => { :user_id => self.id }).group
Query(Tag)
.joins('stories')
.where("user_id = ?")
.group('')
# Q 4021 : # Tag.active.joins(:stories).where
Query(Tag)
.joins('stories')
# Q 4022 : # Tag.active.joins
Query(Tag)

# Q 4023 : # Tag.active
Query(Tag)

# Q 4024 : # ReadRibbon.where(user: @user, story: @story).first_or_create
Query(ReadRibbon)
.where("user = ?")
.where("story = ?")
# Q 4025 : # ReadRibbon.where(user: @user, story: @story).first_or_create
Query(ReadRibbon)
.where("user = ?")
.where("story = ?")
# Q 4026 : # ReadRibbon.where(user: @user, story: @story)
Query(ReadRibbon)
.where("user = ?")
.where("story = ?")
# Q 4027 : # ReadRibbon.where(user: @user, story: @story).first_or_create
Query(ReadRibbon)
.where("user = ?")
.where("story = ?")
# Q 4028 : # user.is_moderator?
Query(User)

# Q 4029 : # user.is_moderator?
Query(User)

# Q 4030 : # self.id
Query(User)

# Q 4031 : # self.id
Query(User)

# Q 4032 : # user.id
Query(User)

# Q 4033 : # self.user_id
Query(Story)
.select('user_id')
# Q 4034 : # user.id
Query(User)

# Q 4035 : # self.user_id
Query(Story)
.select('user_id')
# Q 4036 : # self.is_moderated?
Query(Story)

# Q 4037 : # self.is_moderated?
Query(Story)

# Q 4038 : # self.short_id
Query(Comment)
.select('short_id')
# Q 4039 : # self.short_id
Query(Comment)
.select('short_id')
# Q 4040 : # Tag.arel_table
Query(Tag)

# Q 4041 : # Tag.arel_table
Query(Tag)

# Q 4042 : # self.created_at.to_i
Query(Story)
.select('created_at')
# Q 4043 : # self.created_at
Query(Story)
.select('created_at')
# Q 4044 : # self.created_at.to_i
Query(Story)
.select('created_at')
# Q 4045 : # self.created_at
Query(Story)
.select('created_at')
# Q 4046 : # self.created_at
Query(Comment)
.select('created_at')
# Q 4047 : # self.created_at
Query(Comment)
.select('created_at')
# Q 4048 : # self.created_at
Query(Comment)
.select('created_at')
# Q 4049 : # self.created_at
Query(Comment)
.select('created_at')
# Q 4050 : # self.score
Query(Comment)

# Q 4051 : # self.score
Query(Comment)

# Q 4052 : # self.pushover_user_key.present?
Query(User)

# Q 4053 : # self.pushover_user_key
Query(User)

# Q 4054 : # self.pushover_user_key.present?
Query(User)

# Q 4055 : # self.pushover_user_key
Query(User)

# Q 4056 : # self.pushover_user_key
Query(User)

# Q 4057 : # self.pushover_user_key
Query(User)

# Q 4058 : # self.short_id
Query(Comment)
.select('short_id')
# Q 4059 : # self.short_id
Query(Comment)
.select('short_id')
# Q 4060 : # self.user.is_banned?
Query(User)
.where("id = ?")
# Q 4061 : # self.user
Query(User)
.where("id = ?")
# Q 4062 : # self.user.is_banned?
Query(User)
.where("id = ?")
# Q 4063 : # self.user
Query(User)
.where("id = ?")
# Q 4064 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck(:thread_id)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
.select('thread_id')
# Q 4065 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck(:thread_id)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
.select('thread_id')
# Q 4066 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4067 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC").limit(amount)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4068 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC").limit
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4069 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC")
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
# Q 4070 : # self.comments.active.group(:thread_id).order
Query(Comment)
.where("user_id = ?")
.group('thread_id')
# Q 4071 : # self.comments.active.group(:thread_id)
Query(Comment)
.where("user_id = ?")
.group('thread_id')
# Q 4072 : # self.comments.active.group
Query(Comment)
.where("user_id = ?")
.group('')
# Q 4073 : # self.comments.active
Query(Comment)
.where("user_id = ?")
# Q 4074 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 4075 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC").limit(amount).pluck
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4076 : # self.comments.active.group(:thread_id).order("MAX(created_at) DESC").limit
Query(Comment)
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4077 : # self.comments.active.group(:thread_id).order
Query(Comment)
.where("user_id = ?")
.group('thread_id')
# Q 4078 : # self.comments.active.group
Query(Comment)
.where("user_id = ?")
.group('')
# Q 4079 : # self.comments.active
Query(Comment)
.where("user_id = ?")
# Q 4080 : # self.comments
Query(Comment)
.where("user_id = ?")
# Q 4081 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 4082 : # self.story
Query(Story)
.where("id = ?")
# Q 4083 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 4084 : # self.story
Query(Story)
.where("id = ?")
# Q 4085 : # HiddenStory.where(:user_id => user.id, :story_id => self.id).first
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
.return_limit('1')
# Q 4086 : # HiddenStory.where(:user_id => user.id, :story_id => self.id)
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 4087 : # user.id
Query(User)

# Q 4088 : # self.id
Query(Story)

# Q 4089 : # HiddenStory.where(:user_id => user.id, :story_id => self.id).first
Query(HiddenStory)
.where("user_id = ?")
.where("story_id = ?")
.return_limit('1')
# Q 4090 : # user.id
Query(User)

# Q 4091 : # self.id
Query(Story)

# Q 4092 : # self.show_submitted_story_threads
Query(User)

# Q 4093 : # self.show_submitted_story_threads
Query(User)

# Q 4094 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount).pluck(:thread_id)
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
.select('thread_id')
# Q 4095 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount).pluck
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4096 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount)
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4097 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4098 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC")
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
# Q 4099 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
# Q 4100 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id)
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
# Q 4101 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('')
# Q 4102 : # Comment.joins(:story).where(:stories => { :user_id => self.id })
Query(Comment)
.joins('story')
.where("user_id = ?")
# Q 4103 : # Comment.joins(:story).where
Query(Comment)
.joins('story')
# Q 4104 : # Comment.joins(:story)
Query(Comment)
.joins('story')
# Q 4105 : # Comment.joins
Query(Comment)

# Q 4106 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit(amount).pluck
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4107 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order("MAX(comments.created_at) DESC").limit
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
.order('id')
.order('created_at')
.return_limit('')
# Q 4108 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group(:thread_id).order
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('thread_id')
# Q 4109 : # Comment.joins(:story).where(:stories => { :user_id => self.id }).group
Query(Comment)
.joins('story')
.where("user_id = ?")
.group('')
# Q 4110 : # Comment.joins(:story).where
Query(Comment)
.joins('story')
# Q 4111 : # Comment.joins
Query(Comment)

# Q 4112 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 4113 : # self.story
Query(Story)
.where("id = ?")
# Q 4114 : # self.short_id
Query(Comment)
.select('short_id')
# Q 4115 : # self.story.comments_url
Query(Story)
.where("id = ?")
# Q 4116 : # self.story
Query(Story)
.where("id = ?")
# Q 4117 : # self.short_id
Query(Comment)
.select('short_id')
# Q 4118 : # self.id
Query(User)

# Q 4119 : # self.id
Query(User)

# Q 4120 : # self.created_at
Query(Story)
.select('created_at')
# Q 4121 : # self.created_at
Query(Story)
.select('created_at')
# Q 4122 : # SavedStory.where(:user_id => user.id, :story_id => self.id).first
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
.return_limit('1')
# Q 4123 : # SavedStory.where(:user_id => user.id, :story_id => self.id)
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
# Q 4124 : # user.id
Query(User)

# Q 4125 : # self.id
Query(Story)

# Q 4126 : # SavedStory.where(:user_id => user.id, :story_id => self.id).first
Query(SavedStory)
.where("user_id = ?")
.where("story_id = ?")
.return_limit('1')
# Q 4127 : # user.id
Query(User)

# Q 4128 : # self.id
Query(Story)

# Q 4129 : # self.votes.each
Query(Vote)
.where("comment_id = ?")
# Q 4130 : # self.votes
Query(Vote)
.where("comment_id = ?")
# Q 4131 : # self.votes.each
Query(Vote)
.where("comment_id = ?")
# Q 4132 : # self.votes
Query(Vote)
.where("comment_id = ?")
# Q 4133 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 4134 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 4135 : # Keystore.value_for
Query(Keystore)

# Q 4136 : # self.id
Query(User)

# Q 4137 : # Keystore.value_for
Query(Keystore)

# Q 4138 : # self.id
Query(User)

# Q 4139 : # self.is_unavailable
Query(Story)

# Q 4140 : # self.is_unavailable
Query(Story)

# Q 4141 : # user.is_moderator?
Query(User)

# Q 4142 : # user.is_moderator?
Query(User)

# Q 4143 : # user.id
Query(User)

# Q 4144 : # self.user_id
Query(Story)
.select('user_id')
# Q 4145 : # self.is_moderated?
Query(Story)

# Q 4146 : # user.id
Query(User)

# Q 4147 : # self.user_id
Query(Story)
.select('user_id')
# Q 4148 : # self.is_moderated?
Query(Story)

# Q 4149 : # self.user_id
Query(Comment)
.select('user_id')
# Q 4150 : # self.user_id
Query(Comment)
.select('user_id')
# Q 4151 : # self.save!
Query(User)

# Q 4152 : # self.save!
Query(User)

# Q 4153 : # Moderation.new
Query(Moderation)

# Q 4154 : # Moderation.new
Query(Moderation)

# Q 4155 : # Moderation.new
Query(Moderation)

# Q 4156 : # self.id
Query(User)

# Q 4157 : # self.id
Query(User)

# Q 4158 : # self.id
Query(User)

# Q 4159 : # self.new_record?
Query(Story)

# Q 4160 : # self.new_record?
Query(Story)

# Q 4161 : # self.editing_from_suggestions
Query(Story)

# Q 4162 : # self.editor
Query(Story)

# Q 4163 : # self.editor.id
Query(Story)

# Q 4164 : # self.editor
Query(Story)

# Q 4165 : # self.user_id
Query(Story)
.select('user_id')
# Q 4166 : # self.editing_from_suggestions
Query(Story)

# Q 4167 : # self.editor
Query(Story)

# Q 4168 : # self.editor.id
Query(Story)

# Q 4169 : # self.editor
Query(Story)

# Q 4170 : # self.user_id
Query(Story)
.select('user_id')
# Q 4171 : # self.changes.merge(self.tagging_changes)
Query(Story)

# Q 4172 : # self.changes.merge(self.tagging_changes)
Query(Story)

# Q 4173 : # self.changes.merge
Query(Story)

# Q 4174 : # self.changes
Query(Story)

# Q 4175 : # self.tagging_changes
Query(Story)

# Q 4176 : # self.changes.merge
Query(Story)

# Q 4177 : # self.changes
Query(Story)

# Q 4178 : # self.tagging_changes
Query(Story)

# Q 4179 : # user.is_moderator?
Query(User)

# Q 4180 : # user.is_moderator?
Query(User)

# Q 4181 : # User.transaciton
Query(User)

# Q 4182 : # User.transaciton
Query(User)

# Q 4183 : # user.id
Query(User)

# Q 4184 : # self.user_id
Query(Comment)
.select('user_id')
# Q 4185 : # user.id
Query(User)

# Q 4186 : # self.user_id
Query(Comment)
.select('user_id')
# Q 4187 : # Moderation.new
Query(Moderation)

# Q 4188 : # Moderation.new
Query(Moderation)

# Q 4189 : # Moderation.new
Query(Moderation)

# Q 4190 : # self.id
Query(Comment)

# Q 4191 : # self.id
Query(Comment)

# Q 4192 : # self.id
Query(Comment)

# Q 4193 : # self.save!
Query(User)

# Q 4194 : # self.save!
Query(User)

# Q 4195 : # self.save!
Query(User)

# Q 4196 : # Moderation.new
Query(Moderation)

# Q 4197 : # Moderation.new
Query(Moderation)

# Q 4198 : # Moderation.new
Query(Moderation)

# Q 4199 : # user.id
Query(User)

# Q 4200 : # user.id
Query(User)

# Q 4201 : # user.id
Query(User)

# Q 4202 : # self.editing_from_suggestions
Query(Story)

# Q 4203 : # self.editing_from_suggestions
Query(Story)

# Q 4204 : # Moderation.new
Query(Moderation)

# Q 4205 : # Moderation.new
Query(Moderation)

# Q 4206 : # m = Moderation.new
Query(Moderation)

# Q 4207 : # Moderation.new
Query(Moderation)

# Q 4208 : # self.id
Query(User)

# Q 4209 : # self.id
Query(User)

# Q 4210 : # self.id
Query(User)

# Q 4211 : # self.editor.try(:id)
Query(Story)
.select('id')
# Q 4212 : # self.editor.try(:id)
Query(Story)
.select('id')
# Q 4213 : # self.editor.try
Query(Story)

# Q 4214 : # self.editor
Query(Story)

# Q 4215 : # self.editor.try
Query(Story)

# Q 4216 : # self.editor
Query(Story)

# Q 4217 : # self.id
Query(Story)

# Q 4218 : # self.id
Query(Story)

# Q 4219 : # self.id
Query(Story)

# Q 4220 : # self.save(:validate => false)
Query(Comment)

# Q 4221 : # self.save
Query(Comment)

# Q 4222 : # self.save
Query(Comment)

# Q 4223 : # self.is_expired?
Query(Story)

# Q 4224 : # self.is_expired?
Query(Story)

# Q 4225 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 4226 : # self.story
Query(Story)
.where("id = ?")
# Q 4227 : # self.story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 4228 : # self.story
Query(Story)
.where("id = ?")
# Q 4229 : # self.is_expired?
Query(Story)

# Q 4230 : # self.is_expired?
Query(Story)

# Q 4231 : # self.user.update_comments_posted_count!
Query(User)
.where("id = ?")
# Q 4232 : # self.user
Query(User)
.where("id = ?")
# Q 4233 : # self.user.update_comments_posted_count!
Query(User)
.where("id = ?")
# Q 4234 : # self.user
Query(User)
.where("id = ?")
# Q 4235 : # self.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 4236 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4237 : # self.merged_into_story.short_id
Query(Story)
.where("id = ?")
.select('short_id')
# Q 4238 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4239 : # self.merged_into_story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 4240 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4241 : # self.merged_into_story.title
Query(Story)
.where("id = ?")
.select('title')
# Q 4242 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4243 : # Keystore.value_for
Query(Keystore)

# Q 4244 : # self.id
Query(User)

# Q 4245 : # Keystore.value_for
Query(Keystore)

# Q 4246 : # self.id
Query(User)

# Q 4247 : # Keystore.put
Query(Keystore)

# Q 4248 : # self.id
Query(User)

# Q 4249 : # Keystore.put
Query(Keystore)

# Q 4250 : # self.id
Query(User)

# Q 4251 : # self.received_messages.unread.count
Query(Message)
.where("user_id = ?")
# Q 4252 : # self.received_messages.unread
Query(Message)
.where("user_id = ?")
# Q 4253 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 4254 : # self.received_messages.unread.count
Query(Message)
.where("user_id = ?")
# Q 4255 : # self.received_messages.unread
Query(Message)
.where("user_id = ?")
# Q 4256 : # self.received_messages
Query(Message)
.where("user_id = ?")
# Q 4257 : # self.moderation_reason
Query(Story)

# Q 4258 : # self.moderation_reason
Query(Story)

# Q 4259 : # self.moderation_reason
Query(Story)

# Q 4260 : # ReplyingComment.where(user_id: self.id, is_unread: true).count
Query(ReplyingComment)
.where("user_id = ?")
.where("is_unread = ?")
# Q 4261 : # ReplyingComment.where(user_id: self.id, is_unread: true)
Query(ReplyingComment)
.where("user_id = ?")
.where("is_unread = ?")
# Q 4262 : # self.id
Query(User)

# Q 4263 : # ReplyingComment.where(user_id: self.id, is_unread: true).count
Query(ReplyingComment)
.where("user_id = ?")
.where("is_unread = ?")
# Q 4264 : # self.id
Query(User)

# Q 4265 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id").order("id DESC")
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
.order('id')
.order('id')
# Q 4266 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id").order
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 4267 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id")
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 4268 : # self.votes.joins(:story, :comment).where
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 4269 : # self.votes.joins(:story, :comment)
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 4270 : # self.votes.joins
Query(Vote)
.where("user_id = ?")
# Q 4271 : # self.votes
Query(Vote)
.where("user_id = ?")
# Q 4272 : # self.votes.joins(:story, :comment).where("comments.user_id <> votes.user_id AND " << "stories.user_id <> votes.user_id").order
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 4273 : # self.votes.joins(:story, :comment).where
Query(Vote)
.where("user_id = ?")
.joins('story')
.joins('comment')
# Q 4274 : # self.votes.joins
Query(Vote)
.where("user_id = ?")
# Q 4275 : # self.votes
Query(Vote)
.where("user_id = ?")
# Q 4276 : # Keystore.increment_value_for
Query(Keystore)

# Q 4277 : # self.user_id
Query(Story)
.select('user_id')
# Q 4278 : # Keystore.increment_value_for
Query(Keystore)

# Q 4279 : # self.user_id
Query(Story)
.select('user_id')
# Q 4280 : # Comment.where(:story_id => Story.select(:id).where(:merged_story_id => self.id) + [self.id])
Query(Comment)
.where("story_id = ?")
# Q 4281 : # Story.select(:id).where(:merged_story_id => self.id)
Query(Story)
.select('id')
.where("merged_story_id = ?")
# Q 4282 : # Story.select(:id).where
Query(Story)
.select('id')
# Q 4283 : # Story.select(:id)
Query(Story)
.select('id')
# Q 4284 : # Story.select
Query(Story)

# Q 4285 : # Story.select(:id).where
Query(Story)
.select('id')
# Q 4286 : # Story.select
Query(Story)

# Q 4287 : # self.id
Query(Story)

# Q 4288 : # self.id
Query(Story)

# Q 4289 : # self.id
Query(Story)

# Q 4290 : # self.id
Query(Story)

# Q 4291 : # Story.where(:short_id => sid).first.id
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 4292 : # Story.where(:short_id => sid).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 4293 : # Story.where(:short_id => sid)
Query(Story)
.where("short_id = ?")
# Q 4294 : # Story.where(:short_id => sid).first.id
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 4295 : # Story.where(:short_id => sid).first
Query(Story)
.where("short_id = ?")
.return_limit('1')
# Q 4296 : # self.merged_story_id
Query(Story)
.select('merged_story_id')
# Q 4297 : # self.merged_into_story.try(:short_id)
Query(Story)
.where("id = ?")
.select('short_id')
# Q 4298 : # self.merged_into_story.try
Query(Story)
.where("id = ?")
# Q 4299 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4300 : # self.merged_story_id
Query(Story)
.select('merged_story_id')
# Q 4301 : # self.merged_into_story.try
Query(Story)
.where("id = ?")
# Q 4302 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4303 : # Vote.vote_thusly_on_story_or_comment_for_user_because(1, self.id, nil, self.user_id, nil, false)
Query(Vote)

# Q 4304 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 4305 : # self.id
Query(Story)

# Q 4306 : # Vote.vote_thusly_on_story_or_comment_for_user_because
Query(Vote)

# Q 4307 : # self.id
Query(Story)

# Q 4308 : # self.user_id
Query(Story)
.select('user_id')
# Q 4309 : # self.user_id
Query(Story)
.select('user_id')
# Q 4310 : # self.short_id
Query(Story)
.select('short_id')
# Q 4311 : # self.short_id
Query(Story)
.select('short_id')
# Q 4312 : # self.short_id
Query(Story)
.select('short_id')
# Q 4313 : # self.short_id
Query(Story)
.select('short_id')
# Q 4314 : # self.taggings.sort_by { |t|
#   
#   t.tag.tag
# }.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 4315 : # self.taggings.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 4316 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4317 : # self.taggings.sort_by { |t|
#   
#   t.tag.tag
# }.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 4318 : # self.taggings.sort_by
Query(Tagging)
.where("story_id = ?")
# Q 4319 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4320 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 4321 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 4322 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 4323 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 4324 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 4325 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4326 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 4327 : # self.taggings.reject { |tg|
#   
#   tg.new_record?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 4328 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 4329 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4330 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 4331 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join(" ")
Query(Tagging)
.where("story_id = ?")
# Q 4332 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 4333 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 4334 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 4335 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4336 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map { |tg|
#   
#   tg.tag.tag
# }.join
Query(Tagging)
.where("story_id = ?")
# Q 4337 : # self.taggings.reject { |tg|
#   
#   tg.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 4338 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 4339 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4340 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 4341 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 4342 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4343 : # self.taggings.reject { |t|
#   
#   t.marked_for_destruction?
# }.map
Query(Tagging)
.where("story_id = ?")
# Q 4344 : # self.taggings.reject
Query(Tagging)
.where("story_id = ?")
# Q 4345 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4346 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 4347 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4348 : # self.taggings.each
Query(Tagging)
.where("story_id = ?")
# Q 4349 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4350 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 4351 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 4352 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 4353 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 4354 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 4355 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 4356 : # tagging.mark_for_destruction
Query(Tagging)

# Q 4357 : # tagging.mark_for_destruction
Query(Tagging)

# Q 4358 : # tagging.mark_for_destruction
Query(Tagging)

# Q 4359 : # tagging.mark_for_destruction
Query(Tagging)

# Q 4360 : # self.tags.exists?(:tag => tag_name)
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 4361 : # self.tags.exists?
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 4362 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 4363 : # self.tags.exists?(:tag => tag_name)
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 4364 : # self.tags.exists?
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 4365 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 4366 : # self.tags.exists?
Query(Tag)
.where("story_id = ?")
.return_limit('1')
# Q 4367 : # self.tags
Query(Tag)
.where("story_id = ?")
# Q 4368 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4369 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4370 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 4371 : # Tag.active.where
Query(Tag)

# Q 4372 : # Tag.active
Query(Tag)

# Q 4373 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4374 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 4375 : # Tag.active.where
Query(Tag)

# Q 4376 : # Tag.active
Query(Tag)

# Q 4377 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4378 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 4379 : # Tag.active.where
Query(Tag)

# Q 4380 : # Tag.active
Query(Tag)

# Q 4381 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4382 : # Tag.active.where
Query(Tag)

# Q 4383 : # Tag.active
Query(Tag)

# Q 4384 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 4385 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 4386 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4387 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 4388 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4389 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 4390 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4391 : # tg = self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 4392 : # self.taggings.build
Query(Tagging)
.where("story_id = ?")
# Q 4393 : # self.taggings
Query(Tagging)
.where("story_id = ?")
# Q 4394 : # self.suggested_taggings.where(:user_id => user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 4395 : # self.suggested_taggings.where(:user_id => user.id)
Query(SuggestedTagging)
.where("story_id = ?")
.where("user_id = ?")
# Q 4396 : # self.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4397 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4398 : # user.id
Query(User)

# Q 4399 : # self.suggested_taggings.where
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4400 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4401 : # user.id
Query(User)

# Q 4402 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 4403 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 4404 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 4405 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 4406 : # tagging.tag.tag
Query(Tag)
.where("id = ?")
.select('tag')
# Q 4407 : # tagging.tag
Query(Tag)
.where("id = ?")
# Q 4408 : # tagging.destroy
Query(Tagging)

# Q 4409 : # tagging.destroy
Query(Tagging)

# Q 4410 : # tagging.destroy
Query(Tagging)

# Q 4411 : # tagging.destroy
Query(Tagging)

# Q 4412 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4413 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4414 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 4415 : # Tag.active.where
Query(Tag)

# Q 4416 : # Tag.active
Query(Tag)

# Q 4417 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4418 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 4419 : # Tag.active.where
Query(Tag)

# Q 4420 : # Tag.active
Query(Tag)

# Q 4421 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4422 : # Tag.active.where(:tag => tag_name)
Query(Tag)
.where("tag = ?")
# Q 4423 : # Tag.active.where
Query(Tag)

# Q 4424 : # Tag.active
Query(Tag)

# Q 4425 : # t = Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4426 : # Tag.active.where(:tag => tag_name).first
Query(Tag)
.where("tag = ?")
.return_limit('1')
# Q 4427 : # Tag.active.where
Query(Tag)

# Q 4428 : # Tag.active
Query(Tag)

# Q 4429 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4430 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4431 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4432 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4433 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4434 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4435 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4436 : # tg = self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4437 : # self.suggested_taggings.build
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4438 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4439 : # user.id
Query(User)

# Q 4440 : # user.id
Query(User)

# Q 4441 : # user.id
Query(User)

# Q 4442 : # user.id
Query(User)

# Q 4443 : # user.id
Query(User)

# Q 4444 : # self.suggested_taggings.group_by(&:user_id).each
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4445 : # self.suggested_taggings.group_by(&:user_id)
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4446 : # self.suggested_taggings.group_by
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4447 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4448 : # self.suggested_taggings.group_by(&:user_id).each
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4449 : # self.suggested_taggings.group_by
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4450 : # self.suggested_taggings
Query(SuggestedTagging)
.where("story_id = ?")
# Q 4451 : # self.tags_a.sort
Query(Story)

# Q 4452 : # self.tags_a
Query(Story)

# Q 4453 : # self.tags_a.sort
Query(Story)

# Q 4454 : # self.tags_a
Query(Story)

# Q 4455 : # self.id
Query(Story)

# Q 4456 : # self.id
Query(Story)

# Q 4457 : # self.tags_a.inspect
Query(Story)

# Q 4458 : # self.tags_a
Query(Story)

# Q 4459 : # self.tags_a.inspect
Query(Story)

# Q 4460 : # self.tags_a
Query(Story)

# Q 4461 : # self.save
Query(Story)

# Q 4462 : # self.save
Query(Story)

# Q 4463 : # self.id
Query(Story)

# Q 4464 : # self.id
Query(Story)

# Q 4465 : # self.errors.inspect
Query(Story)

# Q 4466 : # self.errors
Query(Story)

# Q 4467 : # self.errors.inspect
Query(Story)

# Q 4468 : # self.errors
Query(Story)

# Q 4469 : # self.suggested_titles.where(:user_id => user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 4470 : # self.suggested_titles.where(:user_id => user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 4471 : # self.suggested_titles.where(:user_id => user.id)
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
# Q 4472 : # self.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4473 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4474 : # user.id
Query(User)

# Q 4475 : # self.suggested_titles.where(:user_id => user.id).first
Query(SuggestedTitle)
.where("story_id = ?")
.where("user_id = ?")
.return_limit('1')
# Q 4476 : # self.suggested_titles.where
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4477 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4478 : # user.id
Query(User)

# Q 4479 : # self.suggested_titles.build
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4480 : # self.suggested_titles.build
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4481 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4482 : # self.suggested_titles.build
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4483 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4484 : # user.id
Query(User)

# Q 4485 : # user.id
Query(User)

# Q 4486 : # user.id
Query(User)

# Q 4487 : # self.suggested_titles.each
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4488 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4489 : # self.suggested_titles.each
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4490 : # self.suggested_titles
Query(SuggestedTitle)
.where("story_id = ?")
# Q 4491 : # self.id
Query(Story)

# Q 4492 : # self.id
Query(Story)

# Q 4493 : # self.id
Query(Story)

# Q 4494 : # self.id
Query(Story)

# Q 4495 : # self.title.inspect
Query(Story)
.select('title')
# Q 4496 : # self.title
Query(Story)
.select('title')
# Q 4497 : # self.title.inspect
Query(Story)
.select('title')
# Q 4498 : # self.title
Query(Story)
.select('title')
# Q 4499 : # self.title.inspect
Query(Story)
.select('title')
# Q 4500 : # self.title.inspect
Query(Story)
.select('title')
# Q 4501 : # self.title
Query(Story)
.select('title')
# Q 4502 : # self.save
Query(Story)

# Q 4503 : # self.save
Query(Story)

# Q 4504 : # self.save
Query(Story)

# Q 4505 : # self.save
Query(Story)

# Q 4506 : # self.id
Query(Story)

# Q 4507 : # self.id
Query(Story)

# Q 4508 : # self.id
Query(Story)

# Q 4509 : # self.id
Query(Story)

# Q 4510 : # self.id
Query(Story)

# Q 4511 : # self.errors.inspect
Query(Story)

# Q 4512 : # self.errors
Query(Story)

# Q 4513 : # self.errors.inspect
Query(Story)

# Q 4514 : # self.errors
Query(Story)

# Q 4515 : # self.errors.inspect
Query(Story)

# Q 4516 : # self.errors
Query(Story)

# Q 4517 : # self.errors.inspect
Query(Story)

# Q 4518 : # self.errors
Query(Story)

# Q 4519 : # self.short_id
Query(Story)
.select('short_id')
# Q 4520 : # self.short_id
Query(Story)
.select('short_id')
# Q 4521 : # self.is_unavailable
Query(Story)

# Q 4522 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 4523 : # self.is_unavailable
Query(Story)

# Q 4524 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 4525 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 4526 : # self.is_unavailable
Query(Story)

# Q 4527 : # self.unavailable_at
Query(Story)
.select('unavailable_at')
# Q 4528 : # self.is_unavailable
Query(Story)

# Q 4529 : # self.merged_comments.arrange_for_user(nil)
Query(Story)

# Q 4530 : # self.merged_comments.arrange_for_user(nil)
Query(Story)

# Q 4531 : # self.merged_comments.arrange_for_user
Query(Story)

# Q 4532 : # self.merged_comments
Query(Story)

# Q 4533 : # self.merged_comments.arrange_for_user
Query(Story)

# Q 4534 : # self.merged_comments
Query(Story)

# Q 4535 : # comments.count
Query(Comment)

# Q 4536 : # comments.count
Query(Comment)

# Q 4537 : # self.recalculate_hotness!
Query(Story)

# Q 4538 : # self.recalculate_hotness!
Query(Story)

# Q 4539 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4540 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4541 : # self.merged_into_story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 4542 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4543 : # self.merged_into_story.update_comments_count!
Query(Story)
.where("id = ?")
# Q 4544 : # self.merged_into_story
Query(Story)
.where("id = ?")
# Q 4545 : # self.new_record?
Query(Story)

# Q 4546 : # self.new_record?
Query(Story)

# Q 4547 : # user.is_moderator?
Query(User)

# Q 4548 : # self.url.present?
Query(Story)
.select('url')
# Q 4549 : # self.url
Query(Story)
.select('url')
# Q 4550 : # user.is_moderator?
Query(User)

# Q 4551 : # self.url.present?
Query(Story)
.select('url')
# Q 4552 : # self.url
Query(Story)
.select('url')
# Q 4553 : # self.url.blank?
Query(Story)
.select('url')
# Q 4554 : # self.url
Query(Story)
.select('url')
# Q 4555 : # self.comments_path
Query(Story)

# Q 4556 : # self.url
Query(Story)
.select('url')
# Q 4557 : # self.url.blank?
Query(Story)
.select('url')
# Q 4558 : # self.url
Query(Story)
.select('url')
# Q 4559 : # self.comments_path
Query(Story)

# Q 4560 : # self.url
Query(Story)
.select('url')
# Q 4561 : # self.url.blank?
Query(Story)
.select('url')
# Q 4562 : # self.url
Query(Story)
.select('url')
# Q 4563 : # self.comments_url
Query(Story)

# Q 4564 : # self.url
Query(Story)
.select('url')
# Q 4565 : # self.url.blank?
Query(Story)
.select('url')
# Q 4566 : # self.url
Query(Story)
.select('url')
# Q 4567 : # self.comments_url
Query(Story)

# Q 4568 : # self.url
Query(Story)
.select('url')
# Q 4569 : # Vote.where(:story_id => self.id, :comment_id => nil).where("vote != 0").each
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
.where(" = ?")
# Q 4570 : # Vote.where(:story_id => self.id, :comment_id => nil).where("vote != 0")
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
.where(" = ?")
# Q 4571 : # Vote.where(:story_id => self.id, :comment_id => nil).where
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
# Q 4572 : # Vote.where(:story_id => self.id, :comment_id => nil)
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
# Q 4573 : # self.id
Query(Story)

# Q 4574 : # Vote.where(:story_id => self.id, :comment_id => nil).where("vote != 0").each
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
.where(" = ?")
# Q 4575 : # Vote.where(:story_id => self.id, :comment_id => nil).where
Query(Vote)
.where("story_id = ?")
.where("comment_id = ?")
# Q 4576 : # self.id
Query(Story)

# Q 4577 : # user.is_moderator?
Query(User)

# Q 4578 : # user.is_moderator?
Query(User)

# Q 4579 : # user.is_moderator?
Query(User)

# Q 4580 : # user.is_moderator?
Query(User)

# Q 4581 : # user.is_moderator?
Query(User)

# Q 4582 : # self.url
Query(Story)
.select('url')
# Q 4583 : # self.url
Query(Story)
.select('url')
# Q 4584 : # self.url
Query(Story)
.select('url')
# Q 4585 : # self.url
Query(Story)
.select('url')
# Q 4586 : # self.fetching_ip
Query(Story)

# Q 4587 : # self.fetching_ip
Query(Story)

