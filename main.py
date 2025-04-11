from preswald import playground, text, plotly, connect, get_df, table, query, topbar
import plotly.express as px
import plotly.graph_objects as go

topbar()

text("# Spotify Streaming Insights!")
text("An interactive data visualization dashboard powered by SQL and Plotly, exploring Spotify streaming trends across genres, countries, artists, and platforms. Analyze metrics like total streams, skip rates, average listening durations, and more to uncover global listening behaviors.")

# Load the CSV
connect() # load in all sources, which by default is the sample_csv

# SQL Queries for Analysis

# 1. Top 10 Genres by Total Streams
top_genres_query = """
SELECT Genre, SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY Genre
ORDER BY Total_Streams DESC
LIMIT 10
"""
top_genres_df = query(top_genres_query, "spotify_data")

# 2. Top 10 Countries by Total Streams
top_countries_query = """
SELECT Country, SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY Country
ORDER BY Total_Streams DESC
LIMIT 10
"""
top_countries_df = query(top_countries_query, "spotify_data")

# 3. Average Monthly Listeners by Genre
avg_listeners_genre_query = """
SELECT Genre, AVG("Monthly Listeners (Millions)") AS Avg_Monthly_Listeners
FROM spotify_data
GROUP BY Genre
ORDER BY Avg_Monthly_Listeners DESC
"""
avg_listeners_genre_df = query(avg_listeners_genre_query, "spotify_data")

# 4. Average Stream Duration by Genre
avg_duration_genre_query = """
SELECT Genre, AVG("Avg Stream Duration (Min)") AS Avg_Stream_Duration
FROM spotify_data
GROUP BY Genre
ORDER BY Avg_Stream_Duration DESC
"""
avg_duration_genre_df = query(avg_duration_genre_query, "spotify_data")

# 5. Total Streams by Platform Type
total_streams_platform_query = """
SELECT "Platform Type", SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY "Platform Type"
ORDER BY Total_Streams DESC
"""
total_streams_platform_df = query(total_streams_platform_query, "spotify_data")

# 6. Skip Rate by Genre
skip_rate_genre_query = """
SELECT Genre, AVG("Skip Rate (%)") AS Avg_Skip_Rate
FROM spotify_data
GROUP BY Genre
ORDER BY Avg_Skip_Rate DESC
"""
skip_rate_genre_df = query(skip_rate_genre_query, "spotify_data")

# 7. Total Hours Streamed by Country
total_hours_country_query = """
SELECT Country, SUM("Total Hours Streamed (Millions)") AS Total_Hours_Streamed
FROM spotify_data
GROUP BY Country
ORDER BY Total_Hours_Streamed DESC
LIMIT 10
"""
total_hours_country_df = query(total_hours_country_query, "spotify_data")

# 8. Top 10 Artists by Total Streams
top_artists_query = """
SELECT Artist, SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY Artist
ORDER BY Total_Streams DESC
LIMIT 10
"""
top_artists_df = query(top_artists_query, "spotify_data")

# 9. Total Streams by Release Year
total_streams_year_query = """
SELECT "Release Year", SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY "Release Year"
ORDER BY "Release Year"
"""
total_streams_year_df = query(total_streams_year_query, "spotify_data")

# 10. Average Skip Rate by Platform Type
avg_skip_rate_platform_query = """
SELECT "Platform Type", AVG("Skip Rate (%)") AS Avg_Skip_Rate
FROM spotify_data
GROUP BY "Platform Type"
ORDER BY Avg_Skip_Rate DESC
"""
avg_skip_rate_platform_df = query(avg_skip_rate_platform_query, "spotify_data")

# 11. Top Genre by Country
top_genre_country_query = """
SELECT Country, Genre, SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY Country, Genre
ORDER BY Country, Total_Streams DESC
"""
top_genre_country_df = query(top_genre_country_query, "spotify_data")

# 12. Top Artist by Country
top_artist_country_query = """
SELECT Country, Artist, SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY Country, Artist
ORDER BY Country, Total_Streams DESC
"""
top_artist_country_df = query(top_artist_country_query, "spotify_data")

# 13. Artists and their top countries
artists_top_countries_query = """
SELECT Artist, Country, SUM("Total Streams (Millions)") AS Total_Streams
FROM spotify_data
GROUP BY Artist, Country
ORDER BY Artist, Total_Streams DESC
"""
artists_top_countries_df = query(artists_top_countries_query, "spotify_data")

# 14. Artists and their stream minutes by year
artists_stream_minutes_year_query = """
SELECT Artist, "Release Year", SUM("Total Hours Streamed (Millions)") * 60 AS Total_Stream_Minutes
FROM spotify_data
GROUP BY Artist, "Release Year"
ORDER BY Artist, "Release Year"
"""
artists_stream_minutes_year_df = query(artists_stream_minutes_year_query, "spotify_data")

# Visualizations

# Visualization: Top 10 Genres by Total Streams
fig_genres = px.bar(top_genres_df, x='Genre', y='Total_Streams',
                    title='Top 10 Genres by Total Streams',
                    labels={'Genre': 'Genre', 'Total_Streams': 'Total Streams (Millions)'})
fig_genres.update_layout(template='plotly_white')
plotly(fig_genres)

# Pie Chart: Top 10 Genres by Total Streams
fig_genres_pie = px.pie(top_genres_df, names='Genre', values='Total_Streams',
                        title='Top 10 Genres by Total Streams')
fig_genres_pie.update_layout(template='plotly_white')
plotly(fig_genres_pie)

# Visualization: Top 10 Countries by Total Streams
fig_countries = px.bar(top_countries_df, x='Country', y='Total_Streams',
                       title='Top 10 Countries by Total Streams',
                       labels={'Country': 'Country', 'Total_Streams': 'Total Streams (Millions)'})
fig_countries.update_layout(template='plotly_white')
plotly(fig_countries)

# Map Visualization: Top 10 Countries by Total Streams
fig_countries_map = px.choropleth(top_countries_df, locations='Country', locationmode='country names', color='Total_Streams',
                                  title='Top 10 Countries by Total Streams',
                                  labels={'Country': 'Country', 'Total_Streams': 'Total Streams (Millions)'})
fig_countries_map.update_layout(template='plotly_white')
plotly(fig_countries_map)

# Visualization: Average Monthly Listeners by Genre
fig_avg_listeners_genre = px.bar(avg_listeners_genre_df, x='Genre', y='Avg_Monthly_Listeners',
                                 title='Average Monthly Listeners by Genre',
                                 labels={'Genre': 'Genre', 'Avg_Monthly_Listeners': 'Average Monthly Listeners (Millions)'})
fig_avg_listeners_genre.update_layout(template='plotly_white')
plotly(fig_avg_listeners_genre)

# Box Plot: Average Monthly Listeners by Genre
fig_avg_listeners_genre_box = px.box(avg_listeners_genre_df, x='Genre', y='Avg_Monthly_Listeners',
                                     title='Distribution of Monthly Listeners by Genre',
                                     labels={'Genre': 'Genre', 'Avg_Monthly_Listeners': 'Average Monthly Listeners (Millions)'})
fig_avg_listeners_genre_box.update_layout(template='plotly_white')
plotly(fig_avg_listeners_genre_box)

# Visualization: Average Stream Duration by Genre
fig_avg_duration_genre = px.bar(avg_duration_genre_df, x='Genre', y='Avg_Stream_Duration',
                                title='Average Stream Duration by Genre',
                                labels={'Genre': 'Genre', 'Avg_Stream_Duration': 'Average Stream Duration (Min)'})
fig_avg_duration_genre.update_layout(template='plotly_white')
plotly(fig_avg_duration_genre)

# Violin Plot: Average Stream Duration by Genre
fig_avg_duration_genre_violin = px.violin(avg_duration_genre_df, x='Genre', y='Avg_Stream_Duration',
                                          title='Distribution of Stream Duration by Genre',
                                          labels={'Genre': 'Genre', 'Avg_Stream_Duration': 'Average Stream Duration (Min)'})
fig_avg_duration_genre_violin.update_layout(template='plotly_white')
plotly(fig_avg_duration_genre_violin)

# Visualization: Total Streams by Platform Type
fig_total_streams_platform = px.pie(total_streams_platform_df, names='Platform Type', values='Total_Streams',
                                    title='Total Streams by Platform Type')
fig_total_streams_platform.update_layout(template='plotly_white')
plotly(fig_total_streams_platform)

# Bar Chart: Total Streams by Platform Type
fig_total_streams_platform_bar = px.bar(total_streams_platform_df, x='Platform Type', y='Total_Streams',
                                        title='Total Streams by Platform Type',
                                        labels={'Platform Type': 'Platform Type', 'Total_Streams': 'Total Streams (Millions)'})
fig_total_streams_platform_bar.update_layout(template='plotly_white')
plotly(fig_total_streams_platform_bar)

# Visualization: Skip Rate by Genre
fig_skip_rate_genre = px.bar(skip_rate_genre_df, x='Genre', y='Avg_Skip_Rate',
                             title='Average Skip Rate by Genre',
                             labels={'Genre': 'Genre', 'Avg_Skip_Rate': 'Average Skip Rate (%)'})
fig_skip_rate_genre.update_layout(template='plotly_white')
plotly(fig_skip_rate_genre)

# Scatter Plot: Skip Rate by Genre
fig_skip_rate_genre_scatter = px.scatter(skip_rate_genre_df, x='Genre', y='Avg_Skip_Rate',
                                         title='Skip Rate vs. Total Streams by Genre',
                                         labels={'Genre': 'Genre', 'Avg_Skip_Rate': 'Average Skip Rate (%)'})
fig_skip_rate_genre_scatter.update_layout(template='plotly_white')
plotly(fig_skip_rate_genre_scatter)

# Visualization: Total Hours Streamed by Country
fig_total_hours_country = px.bar(total_hours_country_df, x='Country', y='Total_Hours_Streamed',
                                 title='Top 10 Countries by Total Hours Streamed',
                                 labels={'Country': 'Country', 'Total_Hours_Streamed': 'Total Hours Streamed (Millions)'})
fig_total_hours_country.update_layout(template='plotly_white')
plotly(fig_total_hours_country)

# Map Visualization: Total Hours Streamed by Country
fig_total_hours_country_map = px.choropleth(total_hours_country_df, locations='Country', locationmode='country names', color='Total_Hours_Streamed',
                                            title='Top 10 Countries by Total Hours Streamed',
                                            labels={'Country': 'Country', 'Total_Hours_Streamed': 'Total Hours Streamed (Millions)'})
fig_total_hours_country_map.update_layout(template='plotly_white')
plotly(fig_total_hours_country_map)

# Visualization: Top 10 Artists by Total Streams
fig_top_artists = px.bar(top_artists_df, x='Artist', y='Total_Streams',
                         title='Top 10 Artists by Total Streams',
                         labels={'Artist': 'Artist', 'Total_Streams': 'Total Streams (Millions)'})
fig_top_artists.update_layout(template='plotly_white')
plotly(fig_top_artists)

# Pie Chart: Top 10 Artists by Total Streams
fig_top_artists_pie = px.pie(top_artists_df, names='Artist', values='Total_Streams',
                             title='Top 10 Artists by Total Streams')
fig_top_artists_pie.update_layout(template='plotly_white')
plotly(fig_top_artists_pie)

# Visualization: Total Streams by Release Year
fig_total_streams_year = px.line(total_streams_year_df, x='Release Year', y='Total_Streams',
                                 title='Total Streams by Release Year',
                                 labels={'Release Year': 'Release Year', 'Total_Streams': 'Total Streams (Millions)'})
fig_total_streams_year.update_layout(template='plotly_white')
plotly(fig_total_streams_year)

# Bar Chart: Total Streams by Release Year
fig_total_streams_year_bar = px.bar(total_streams_year_df, x='Release Year', y='Total_Streams',
                                    title='Total Streams by Release Year',
                                    labels={'Release Year': 'Release Year', 'Total_Streams': 'Total Streams (Millions)'})
fig_total_streams_year_bar.update_layout(template='plotly_white')
plotly(fig_total_streams_year_bar)

# Visualization: Average Skip Rate by Platform Type
fig_avg_skip_rate_platform = px.bar(avg_skip_rate_platform_df, x='Platform Type', y='Avg_Skip_Rate',
                                    title='Average Skip Rate by Platform Type',
                                    labels={'Platform Type': 'Platform Type', 'Avg_Skip_Rate': 'Average Skip Rate (%)'})
fig_avg_skip_rate_platform.update_layout(template='plotly_white')
plotly(fig_avg_skip_rate_platform)

# Visualization: Top Genre by Country
fig_top_genre_country = px.bar(top_genre_country_df, x='Country', y='Total_Streams', color='Genre',
                               title='Top Genre by Country',
                               labels={'Country': 'Country', 'Total_Streams': 'Total Streams (Millions)', 'Genre': 'Genre'})
fig_top_genre_country.update_layout(template='plotly_white')
plotly(fig_top_genre_country)

# Map Visualization: Top Genre by Country
fig_top_genre_country_map = px.choropleth(top_genre_country_df, locations='Country', locationmode='country names', color='Genre',
                                          title='Top Genre by Country',
                                          labels={'Country': 'Country', 'Genre': 'Genre'})
fig_top_genre_country_map.update_layout(template='plotly_white')
plotly(fig_top_genre_country_map)

# Visualization: Top Artist by Country
fig_top_artist_country = px.bar(top_artist_country_df, x='Country', y='Total_Streams', color='Artist',
                                title='Top Artist by Country',
                                labels={'Country': 'Country', 'Total_Streams': 'Total Streams (Millions)', 'Artist': 'Artist'})
fig_top_artist_country.update_layout(template='plotly_white')
plotly(fig_top_artist_country)

# Map Visualization: Top Artist by Country
fig_top_artist_country_map = px.choropleth(top_artist_country_df, locations='Country', locationmode='country names', color='Artist',
                                           title='Top Artist by Country',
                                           labels={'Country': 'Country', 'Artist': 'Artist'})
fig_top_artist_country_map.update_layout(template='plotly_white')
plotly(fig_top_artist_country_map)

# Visualization: Artists and their top countries
fig_artists_top_countries = px.bar(artists_top_countries_df, x='Artist', y='Total_Streams', color='Country',
                                   title='Artists and their Top Countries',
                                   labels={'Artist': 'Artist', 'Total_Streams': 'Total Streams (Millions)', 'Country': 'Country'})
fig_artists_top_countries.update_layout(template='plotly_white')
plotly(fig_artists_top_countries)

# Heatmap: Artists and their top countries
fig_artists_top_countries_heatmap = go.Figure(data=go.Heatmap(
    z=artists_top_countries_df['Total_Streams'],
    x=artists_top_countries_df['Artist'],
    y=artists_top_countries_df['Country'],
    colorscale='Viridis'
))
fig_artists_top_countries_heatmap.update_layout(
    title='Heatmap of Artists and their Top Countries',
    xaxis_nticks=36,
    template='plotly_white'
)
plotly(fig_artists_top_countries_heatmap)

# Visualization: Artists and their stream minutes by year
fig_artists_stream_minutes_year = px.line(artists_stream_minutes_year_df, x='Release Year', y='Total_Stream_Minutes', color='Artist',
                                          title='Artists and their Stream Minutes by Year',
                                          labels={'Release Year': 'Release Year', 'Total_Stream_Minutes': 'Total Stream Minutes', 'Artist': 'Artist'})
fig_artists_stream_minutes_year.update_layout(template='plotly_white')
plotly(fig_artists_stream_minutes_year)

# Bar Chart: Artists and their stream minutes by year
fig_artists_stream_minutes_year_bar = px.bar(artists_stream_minutes_year_df, x='Release Year', y='Total_Stream_Minutes', color='Artist',
                                             title='Artists and their Stream Minutes by Year',
                                             labels={'Release Year': 'Release Year', 'Total_Stream_Minutes': 'Total Stream Minutes', 'Artist': 'Artist'})
fig_artists_stream_minutes_year_bar.update_layout(template='plotly_white')
plotly(fig_artists_stream_minutes_year_bar)

# Visualization: Playground Raw Data
playground(label="Spotify Stream Data", query='SELECT * FROM spotify_data ORDER BY "Monthly Listeners (Millions)" DESC;')
